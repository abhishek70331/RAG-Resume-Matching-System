# Resume RAG Semantic Matching System

AI-powered resume screening system using Retrieval Augmented Generation.

## Features

- Resume ingestion pipeline
- Intelligent document chunking
- Vector database using ChromaDB
- Semantic job matching
- Hybrid search
- Candidate ranking

## Tech Stack

Python  
Sentence Transformers  
ChromaDB  
LangChain  

## Architecture

Resumes → Chunking → Embeddings → Vector DB  
Job Description → Embedding → Semantic Search → Ranking  

## Dataset

- 30+ resumes
- 5+ job descriptions

## Run the Project

Build vector database:

python src/resume_rag.py

Run job matching:

python src/job_matcher.py