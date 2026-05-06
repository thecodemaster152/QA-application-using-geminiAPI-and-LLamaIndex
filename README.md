# QA Application using Gemini API and LlamaIndex

## Overview
An AI-powered Question Answering application that allows users to upload 
documents and ask questions about them using Google Gemini API and LlamaIndex.

## Tech Stack
- Python 3.11
- Google Gemini API
- LlamaIndex
- Streamlit
- Python-dotenv

## Features
- Upload any document (PDF/TXT)
- Ask questions about the document
- Get AI-powered answers using Gemini
- RAG (Retrieval Augmented Generation) pipeline

## How to run locally

1. Clone the repo

2. Create virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirement.txt

4. Add your API key
Create a .env file and add:
GOOGLE_API_KEY=your_api_key_here

5. Run the app
streamlit run StreamlitApp.py

## Project Structure
- `QA_with_PDF/` - Core application logic
- `Experiments/` - Jupyter notebook experiments
- `StreamlitApp.py` - Web interface
- `Data/` - Sample documents
