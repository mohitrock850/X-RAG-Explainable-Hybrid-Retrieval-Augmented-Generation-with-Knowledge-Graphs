import streamlit as st
from utils import get_pdf_text, get_text_chunks, get_vector_store, extract_entities, user_input
from graph_db import Neo4jConnection

def main():
    st.set_page_config(page_title="Conversational Graph RAG", layout="wide")
    st.title("Conversational Graph RAG 🧠💬")

    # Initialize session state for messages and chat history if they don't exist
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    with st.sidebar:
        st.header("Configuration")
        openai_api_key = st.text_input("OpenAI API Key", type="password", key="openai_key")
        
        st.subheader("Neo4j Credentials")
        neo4j_uri = st.text_input("URI", value="neo4j://localhost:7687", key="neo4j_uri")
        neo4j_user = st.text_input("Username", value="neo4j", key="neo4j_user")
        neo4j_password = st.text_input("Password", type="password", key="neo4j_pass")

        st.subheader("Document Upload")
        pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True, type="pdf")

        if st.button("Process Documents"):
            if not all([pdf_docs, openai_api_key, neo4j_uri, neo4j_user, neo4j_password]):
                st.warning("Please provide all credentials and upload documents.")
            else:
                with st.spinner("Processing documents... This may take a moment."):
                    # Establish graph connection
                    graph_db = Neo4jConnection(neo4j_uri, neo4j_user, neo4j_password)
                    if graph_db.driver is None:
                        st.error("Could not connect to Neo4j. Please check your credentials.")
                        st.stop()
                    
                    st.session_state.graph_db = graph_db
                    
                    # Process documents
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    st.session_state.vector_store = get_vector_store(text_chunks, openai_api_key)

                    # Populate knowledge graph
                    total_entities = 0
                    for chunk in text_chunks:
                        entities = extract_entities(chunk)
                        if entities:
                            graph_db.add_chunk_with_entities(chunk, entities)
                            total_entities += len(entities)
                    
                    st.success(f"Processing complete! Vector store created and {total_entities} entity mentions added to the graph.")

    # --- MAIN CHAT INTERFACE ---
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask a question about your documents..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if "vector_store" not in st.session_state or "graph_db" not in st.session_state:
            st.warning("Please process your documents first.")
        else:
            with st.spinner("Thinking..."):
                graph_db = st.session_state.graph_db
                vector_store = st.session_state.vector_store
                chat_history = st.session_state.chat_history[-4:] # Use last 2 pairs of interactions

                response, docs, graph_chunks = user_input(prompt, vector_store, graph_db, openai_api_key, chat_history)

                with st.chat_message("assistant"):
                    st.markdown(response)
                    with st.expander("Show Retrieved Evidence"):
                        st.subheader("📄 From Vector Search")
                        if docs:
                            for doc in docs:
                                st.info(doc.page_content)
                        else:
                            st.write("No relevant documents found from vector search.")

                        st.subheader("🔗 From Knowledge Graph")
                        if graph_chunks:
                            for chunk in graph_chunks:
                                st.success(chunk)
                        else:
                            st.write("No relevant context was found in the knowledge graph for the search terms.")

                # Update session state
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.session_state.chat_history.append({"role": "user", "content": prompt})
                st.session_state.chat_history.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()