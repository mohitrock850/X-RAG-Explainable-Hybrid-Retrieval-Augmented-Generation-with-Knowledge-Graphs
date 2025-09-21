# X-RAG: Explainable Hybrid Retrieval-Augmented Generation 🧠💬

<div align="center">

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LangChain](https://img.shields.io/badge/Powered%20By-LangChain-blue)](https://www.langchain.com/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-orange)](https://streamlit.io)
[![Neo4j](https://img.shields.io/badge/Database-Neo4j-008cc1)](https://neo4j.com)

</div>

An advanced Retrieval-Augmented Generation (RAG) system that answers questions based on uploaded PDF documents. It uniquely combines the power of semantic vector search with structured knowledge graph retrieval to provide highly accurate, context-aware, and explainable answers.

<br>
<p align="center">
  <img src="screenshots/main.png" alt="Application Screenshot" width="800">
</p>

## Table of Contents

- [About The Project](#about-the-project)
- [Key Features](#key-features)
- [How It Works](#how-it-works)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Documents Tested](#documents-tested)

## About The Project

Traditional RAG systems rely solely on semantic similarity, which can sometimes miss structured facts or relationships within a document. X-RAG enhances this process by building a dynamic **Knowledge Graph** on the fly. This hybrid approach allows the system to not only find semantically relevant text chunks but also query for explicit relationships between entities, leading to more robust and comprehensive answers.

## Key Features

-   **🧠 Hybrid Retrieval:** Fuses **FAISS** vector search for semantic context with **Neo4j** graph search for factual, entity-based relationships.
-   **✨ Dynamic Knowledge Graph:** Automatically extracts key entities from documents using **spaCy** and populates them into a graph structure in real-time.
-   **💬 Conversational Memory:** Remembers the context of recent interactions, allowing for natural, follow-up questions.
-   **🔬 Explainable AI (XAI):** For transparency, the application displays the exact source chunks retrieved from both the vector store and the knowledge graph that were used to formulate the answer.
-   **🚀 Interactive UI:** A clean and user-friendly interface built with **Streamlit** for easy document uploads and conversational Q&A.

## How It Works

The application follows a complete RAG pipeline from data ingestion to answer generation:

1.  **Data Ingestion**: PDFs are uploaded through the Streamlit interface.
2.  **Text Processing**: The raw text is extracted and split into smaller, manageable chunks.
3.  **Knowledge Base Creation**:
    -   **Vector Store**: Text chunks are converted into embeddings using OpenAI and stored in a FAISS vector store for semantic search.
    -   **Knowledge Graph**: Entities (like names, places, concepts) are extracted from each chunk and stored in a Neo4j graph, linking chunks to the entities they mention.
4.  **Hybrid Retrieval**: When a user asks a question:
    -   The system performs a similarity search against the FAISS vector store.
    -   It also extracts entities from the question and queries the Neo4j graph to find chunks where these entities co-exist.
5.  **Augmented Generation**: The retrieved context from both sources is combined with the user's question and chat history, and sent to an OpenAI model to generate a final, synthesized answer.

## Screenshots

<div align="center">
  <h3>Screenshots</h3>
  <table border="0" cellspacing="10" cellpadding="10">
    <tr>
      <td align="center">
        <strong>Conversational Q&A Interface</strong><br><br>
        <img src="screenshots/image2.png" alt="Full Q&A conversation" width="400">
      </td>
      <td align="center">
        <strong>Easy Configuration & Upload</strong><br><br>
        <img src="screenshots/main.png" alt="Initial application screen with configuration sidebar" width="400">
      </td>
    </tr>
    <tr>
      <td align="center">
        <strong>Evidence from Vector Search</strong><br><br>
        <img src="screenshots/image3.png" alt="Showing retrieved evidence from the vector search" width="400">
      </td>
      <td align="center">
        <strong>Evidence from Knowledge Graph</strong><br><br>
        <img src="screenshots/image4.png" alt="Showing retrieved evidence from the knowledge graph" width="400">
      </td>
    </tr>
  </table>
</div>

## 🛠️ Tech Stack

This project is built with a modern, powerful stack of tools and libraries:

<p align="center">
  <a href="https://www.python.org" target="_blank"> 
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://www.langchain.com/" target="_blank"> 
    <img src="https://img.shields.io/badge/LangChain-4A90E2?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiIgdmlld0JveD0iMCAwIDMyIDMyIj48cGF0aCBmaWxsPSIjZmZmZmZmIiBkPSJNMjggN3YxOGwtNy01VjEybDctNXptLTkgMmwtNyA1djEwbDcgNUwyMyAxMmw0LTNMMTkgOXptLTYgNWw0IDN2OGwtNCAzVjE0eiIvPjwvc3ZnPg==" alt="LangChain">
  </a>
  <a href="https://streamlit.io" target="_blank"> 
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  </a>
  <a href="https://openai.com/" target="_blank"> 
    <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI">
  </a>
  <a href="https://neo4j.com/" target="_blank"> 
    <img src="https://img.shields.io/badge/Neo4j-008cc1?style=for-the-badge&logo=neo4j&logoColor=white" alt="Neo4j">
  </a>
  <a href="https://github.com/facebookresearch/faiss" target="_blank"> 
    <img src="https://img.shields.io/badge/FAISS-3B5998?style=for-the-badge&logo=facebook&logoColor=white" alt="FAISS">
  </a>
  <a href="https://spacy.io/" target="_blank"> 
    <img src="https://img.shields.io/badge/spaCy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white" alt="spaCy">
  </a>
</p>

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

-   Python 3.9+
-   Git
-   Neo4j Desktop (or a running Neo4j instance)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/mohitrock850/X-RAG-Explainable-Hybrid-Retrieval-Augmentation-with-Knowledge-Graphs.git](https://github.com/mohitrock850/X-RAG-Explainable-Hybrid-Retrieval-Augmentation-with-Knowledge-Graphs.git)
    cd X-RAG-Explainable-Hybrid-Retrieval-Augmentation-with-Knowledge-Graphs
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Create the environment
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate
    
    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download the spaCy NLP model:**
    ```bash
    python -m spacy download en_core_web_lg
    ```

## Usage

1.  **Launch the Streamlit application** (ensure your virtual environment is activated):
    ```bash
    streamlit run app.py
    ```
2.  Open your web browser to the local URL provided (usually `http://localhost:8501`).
3.  In the sidebar, enter your **OpenAI API Key** and your **Neo4j Credentials**.
4.  Upload one or more PDF files.
5.  Click the **"Process Documents"** button and wait for the knowledge base to be built.
6.  Start asking questions in the chat box!

## Documents Tested

This system has been successfully tested on complex technical papers, including:
-   `Attention is all You Need.pdf`
-   `ImageNet Classification with Deep CNN.pdf`
