# RocketBot

RocketBot is a Retrieval-Augmented Generation (RAG) chatbot designed to help University of Toledo students quickly find accurate information about courses, academic programs, university policies, campus resources, and other UToledo-related topics.

Instead of relying directly on an Large Language Model (LLM) for hopefully having this kind of knowledge from its training, we utilize relevant public data that UToledo provides to give the LLM further context to allow for better responses.

## Project Goal

University information is spread across course catalogs, department webpages, policy documents, and other university resources. Finding an answer can require searching through several different pages or documents.

RocketBot aims to provide a single interface where students can ask Utoledo related questions such as:

- What are the prerequisites for EECS 3540?
- What courses are required for the Computer Science and Engineering degree?
- How many co-op rotations are required for engineering students?
- What are the requirements to graduate?
- How do I withdraw from a course?
- What academic resources are available to students?

The system retrieves relevant information from official Utoledo sources and uses it to generate a response with references to the original sources.

## How It Works

RocketRAG uses Retrieval-Augmented Generation (RAG).

```text
University of Toledo Data
        │
        ▼
   Data Ingestion
        │
        ▼
  Text Chunking
        │
        ▼
    Embeddings
        │
        ▼
   Vector Database
        │
        │
        ├──────────────────────────┐
        │                          │
        │                   Student Question
        │                          │
        │                          ▼
        │                    Query Embedding
        │                          │
        └──────────────► Vector Similarity Search
                                   │
                                   ▼
                           Relevant Documents
                                   │
                                   ▼
                           LLM + Retrieved Context
                                   │
                                   ▼
                           Answer + Sources
```

When a user asks a question:

1. The question is converted into an embedding.
2. The vector database is searched for semantically similar UToledo information.
3. The most relevant document chunks are retrieved.
4. The retrieved information and the user's question are provided to an LLM.
5. The LLM generates an answer grounded in the retrieved UToledo information.
6. The original sources are displayed with the response.

## Tech Stack

### Frontend

- React
- Vite
- Tailwind CSS

### Backend

- Python
- FastAPI

### RAG / AI

- (embedding model - not established yet)
- (LLM API - not established yet)
- (cross-encoder for reranking? - not established yet)

### Database

- (not established yet)

### Data Collection

- (Toledo website info ingestion)
- PyMuPDF for PDF text parsing
- (Chunking pipeline)

### Deployment

- Cloudflare - frontend
- Render - FastAPI backend

## Data Sources

RocketRAG will use publicly available information from official University of Toledo sources.

Planned data sources include:

- UToledo Undergraduate Course Catalog
- Course descriptions and prerequisites
- Degree and program requirements
- College of Engineering information
- Academic policies
- Co-op information
- Student services and resources
- Financial aid information
- Parking and transportation information
- University webpages and publicly available documents

Each stored document chunk contains metadata identifying its original source so that generated answers can provide citations.

## Project Structure

```text
RAG_PROJECT/
│
├── frontend/
│   └── React application
│
├── backend/
│   ├── main.py
│   ├── api/
│   └── rag/
│
├── ingestion/
│
├── evaluation/
│
└── README.md
```

The project structure may change as development progresses.

## Retrieval

Documents are divided into smaller chunks before being converted into vector embeddings.

Each chunk contains both the text and associated metadata.

Example:

```json
{
    "content": "Course information...",
    "title": "EECS 3540",
    "category": "course",
    "source": "University of Toledo Course Catalog",
    "url": "https://...",
    "academic_year": "2026-2027"
}
```

When a question is submitted, its embedding is compared against stored document embeddings to identify the most relevant information.

Future experiments may compare:

- Dense vector retrieval
- BM25 keyword retrieval
- Hybrid retrieval
- Cross-encoder reranking
- Different chunk sizes
- Different Top-K retrieval values

## Evaluation

RocketBot will be evaluated using a collection of UToledo-specific questions with known relevant sources.

Potential retrieval metrics include:

- Recall@K
- Precision@K
- Mean Reciprocal Rank (MRR)

Generated responses may also be evaluated for:

- Answer correctness
- Faithfulness to retrieved context
- Citation correctness
- Relevance

This allows different RAG configurations to be compared quantitatively instead of evaluating the system only through example conversations.

## Disclaimer

RocketBot is a student project and is not an official University of Toledo service.

Although the system retrieves information from official university sources, generated responses may contain errors or outdated information. Users should verify important academic, financial, or university policy information using the linked official University of Toledo sources.

## Team

Developed as a student project for the University of Toledo.

**Team Members**

- Zackery Hengartner
- Michael Larson
- Nicole Bertoni
- Livia Shrestha

## 📄 License

This project is intended for educational and academic use.