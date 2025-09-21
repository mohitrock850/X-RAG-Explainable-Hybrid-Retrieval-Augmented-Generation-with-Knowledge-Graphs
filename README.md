# X-RAG: Explainable Hybrid Retrieval-Augmented Generation 🧠💬

<div align="center">

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LangChain](https://img.shields.io/badge/Powered%20By-LangChain-blue)](https://www.langchain.com/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-orange)](https://streamlit.io)
[![Neo4j](https://img.shields.io/badge/Database-Neo4j-008cc1)](https://neo4j.com)

</div>

X-RAG is an advanced RAG system that answers questions from PDFs by combining semantic search with a knowledge graph. While traditional RAG relies on similarity alone, X-RAG builds a dynamic **Knowledge Graph** to understand relationships between entities, leading to more accurate, explainable, and context-aware answers.

---

## ⚙️ How It Works

This diagram illustrates the flow from document ingestion to the final, synthesized answer, highlighting the parallel vector and graph retrieval paths.

```mermaid
graph TD
    A[📄 PDFs Upload] --> B(Chunk & Process Text);
    B --> C{Vector Store - FAISS};
    B --> D{Knowledge Graph - Neo4j};
    E[User Query] --> F(Extract Entities);
    E --> C;
    F --> D;
    C --> G((Hybrid Context));
    D --> G;
    G --> H[🧠 LLM - OpenAI];
    I[💬 Chat History] --> H;
    H --> J[✅ Final Answer];

✨ Key Features
🧠 Hybrid Retrieval: Combines semantic search (FAISS) with graph-based fact retrieval (Neo4j).

✨ Dynamic Knowledge Graph: Automatically extracts and links entities from documents using spaCy.

💬 Conversational Memory: Remembers recent interactions for seamless follow-up questions.

🔬 Explainable AI (XAI): Displays the exact source chunks used to generate each answer for full transparency.

🚀 Interactive UI: Clean and simple interface built with Streamlit.

📸 Screenshots
<div align="center">
<table border="0" cellspacing="10" cellpadding="10">
<tr>
<td align="center">
<strong>Conversational Q&A Interface</strong><br><br>
<img src="screenshots/image2.png" alt="Full Q&A conversation" width="400">
</td>
<td align="center">
<strong>Easy Configuration & Upload</strong><br><br>
<img src="screenshots/main.png" alt="Initial application screen" width="400">
</td>
</tr>
<tr>
<td align="center">
<strong>Evidence from Vector Search</strong><br><br>
<img src="screenshots/image3.png" alt="Evidence from vector search" width="400">
</td>
<td align="center">
<strong>Evidence from Knowledge Graph</strong><br><br>
<img src="screenshots/image4.png" alt="Evidence from knowledge graph" width="400">
</td>
</tr>
</table>
</div>

🛠️ Tech Stack
Backend: Python

LLM Orchestration: LangChain

Vector DB: FAISS

Graph DB: Neo4j

LLM: OpenAI

UI: Streamlit

PDF Processing: PyPDF

NLP: spaCy

🚀 Getting Started
Prerequisites
Python 3.9+ & Git

Neo4j Desktop

Installation
Clone the repository:

Bash

git clone [https://github.com/mohitrock850/X-RAG-Explainable-Hybrid-Retrieval-Augmentation-with-Knowledge-Graphs.git](https://github.com/mohitrock850/X-RAG-Explainable-Hybrid-Retrieval-Augmentation-with-Knowledge-Graphs.git)
cd X-RAG-Explainable-Hybrid-Retrieval-Augmentation-with-Knowledge-Graphs
Setup and activate virtual environment:

Bash

python -m venv venv
# Windows: .\venv\Scripts\activate | macOS/Linux: source venv/bin/activate
Install dependencies and NLP model:

Bash

pip install -r requirements.txt
python -m spacy download en_core_web_lg
▶️ Usage
Launch the app (from your activated environment):

Bash

streamlit run app.py
Open the app in your browser.

Enter your OpenAI API Key and Neo4j Credentials in the sidebar.

Upload PDFs, click "Process Documents," and start asking questions!

🔬 Documents Tested
This system was successfully tested on complex technical papers, including:

Attention is all You Need.pdf

ImageNet Classification with Deep CNN.pdf
