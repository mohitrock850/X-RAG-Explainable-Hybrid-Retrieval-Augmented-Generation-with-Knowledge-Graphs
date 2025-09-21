import spacy
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import LLMChain  # Replaced load_qa_chain with LLMChain
from langchain.prompts import PromptTemplate
from pypdf import PdfReader
from graph_db import Neo4jConnection
import re

# Load spaCy model, downloading if necessary
try:
    nlp = spacy.load("en_core_web_lg")
except OSError:
    print("Downloading 'en_core_web_lg' model...")
    spacy.cli.download("en_core_web_lg")
    nlp = spacy.load("en_core_web_lg")

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                # Clean up text by removing excessive newlines and spaces
                text += re.sub(r'\s+', ' ', page_text).strip()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_text(text)

def get_vector_store(text_chunks, api_key):
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    return FAISS.from_texts(text_chunks, embedding=embeddings)

def extract_entities(text):
    """
    Extracts named entities and noun chunks from text.
    """
    doc = nlp(text)
    entities = set()
    
    # Add all named entities
    for ent in doc.ents:
        entities.add(ent.text.strip())
        
    # Add all noun chunks
    for chunk in doc.noun_chunks:
        entities.add(chunk.text.strip())
            
    # Filter out stopwords and very short entities to reduce noise
    final_entities = [
        ent for ent in entities 
        if not nlp.vocab[ent.lower()].is_stop and len(ent) > 2
    ]
                    
    return final_entities

def get_conversational_chain(api_key):
    prompt_template = """
    You are an intelligent assistant. Your goal is to provide a comprehensive and accurate answer based on the user's question, the retrieved context from documents, and the ongoing chat history.

    1. Synthesize information from both the "Vector Context" and "Graph Context".
    2. Prioritize the most relevant details to form a coherent answer.
    3. If the context does not contain the answer, state that the information is not available in the provided documents.
    4. Incorporate the chat history to understand follow-up questions.

    Chat History:
    {chat_history}

    Vector Context:
    {vector_context}

    Graph Context:
    {graph_context}

    Question:
    {question}

    Answer:
    """
    model = ChatOpenAI(temperature=0.4, openai_api_key=api_key)
    prompt = PromptTemplate(
        template=prompt_template, 
        input_variables=["chat_history", "vector_context", "graph_context", "question"]
    )
    # FIX: Use LLMChain directly as it's more flexible for our custom prompt
    chain = LLMChain(llm=model, prompt=prompt)
    return chain

def user_input(user_question, vector_store, graph_db: Neo4jConnection, api_key, chat_history):
    # Vector Search
    docs = vector_store.similarity_search(user_question, k=3)
    vector_context = "\n\n".join([doc.page_content for doc in docs])

    # Graph Search
    doc = nlp(user_question)
    search_terms = list(set([chunk.text.strip() for chunk in doc.noun_chunks] + [ent.text.strip() for ent in doc.ents]))
    search_terms = [term for term in search_terms if not nlp.vocab[term.lower()].is_stop and len(term) > 2]
    
    graph_chunks = []
    if search_terms:
        graph_chunks = graph_db.get_context_for_terms(search_terms)
    
    graph_context = "\n\n".join(graph_chunks)

    # Generate Response
    formatted_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in chat_history])
    chain = get_conversational_chain(api_key)
    
    # FIX: Invoke the chain with the correct input variables defined in our prompt
    response = chain.invoke(
        {
            "vector_context": vector_context,
            "graph_context": graph_context,
            "chat_history": formatted_history, 
            "question": user_question
        }
    )
    
    # FIX: The output from LLMChain is in the 'text' key, not 'output_text'
    return response["text"], docs, graph_chunks