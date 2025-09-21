Of course. Here is a complete and professional README.md file for your project in a single markdown block.

Markdown

# X-RAG: Explainable Hybrid Retrieval-Augmented Generation 🧠💬

This project is an advanced Retrieval-Augmented Generation (RAG) system that answers questions based on uploaded PDF documents. It uniquely combines the power of semantic search from a vector database with structured data retrieval from a knowledge graph, providing more accurate and context-aware answers.

![Application Screenshot](screenshots/image_8cf51e.png)

## Key Features

-   **Hybrid Search:** Leverages both **FAISS** for fast semantic search and a **Neo4j Knowledge Graph** for retrieving structured entity relationships, ensuring a comprehensive context for the language model.
-   **Dynamic Knowledge Graph:** Automatically extracts key entities and concepts from the source documents using **spaCy** and populates them into a Neo4j graph structure on the fly.
-   **Conversational Memory:** Remembers the context of the last few interactions, allowing users to ask natural follow-up questions.
-   **Explainable AI (XAI):** For transparency, the application displays the exact source chunks from both the vector store and the knowledge graph that were used to generate the answer.
-   **Interactive UI:** Built with **Streamlit** for a clean and intuitive user experience, allowing for easy document uploads and conversational queries.

## Tech Stack

-   **Backend:** Python
-   **LLM Orchestration:** LangChain
-   **Vector Database:** FAISS
-   **Graph Database:** Neo4j
-   **Language Model:** OpenAI API
-   **UI Framework:** Streamlit
-   **PDF Processing:** PyPDF
-   **NLP for Entity Extraction:** spaCy

---

## Setup and Installation

Follow these steps to set up and run the project locally.

**1. Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd X-RAG-Knowledge-Graph
2. Create a virtual environment and install dependencies:
It is highly recommended to use a virtual environment to manage project dependencies.

Bash

# Create the virtual environment
python -m venv venv

# Activate the environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt
3. Download the spaCy NLP model:
The application uses a spaCy model for entity extraction. Download it with the following command:

Bash

python -m spacy download en_core_web_lg
4. Set up Neo4j:

Ensure you have a running Neo4j instance (this can be easily done using Neo4j Desktop).

Make sure the database is active and you have the URI, username, and password ready.

How to Run
1. Launch the Streamlit application:
Make sure your virtual environment is activated, then run the following command in your terminal:

Bash

streamlit run app.py
2. Use the application:

Open your web browser to the local URL provided by Streamlit (usually http://localhost:8501).

In the sidebar, enter your OpenAI API Key and your Neo4j Credentials.

Upload one or more PDF files using the file uploader.

Click the "Process Documents" button and wait for the knowledge base to be built.

Once processing is complete, you can start asking questions in the chat interface!