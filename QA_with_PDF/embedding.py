from llama_index.core import VectorStoreIndex
from llama_index.core import Settings
from llama_index.core import StorageContext
from llama_index.embeddings.gemini import GeminiEmbedding

from QA_with_PDF.data_ingestion import load_data_from_directory
from QA_with_PDF.model_api import load_model

import sys
from logger import logging
from exception import customexception

def download_gemini_embedding_model(model, document):
    try:
        logging.info("Initializing Gemini embedding model")
        
        gemini_embed_model = GeminiEmbedding(
            model_name="models/gemini-embedding-001"
        )
        
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.chunk_size = 512
        Settings.chunk_overlap = 50
        
        logging.info("Creating vector store index from documents")
        
        index = VectorStoreIndex.from_documents(document)
        index.storage_context.persist()
        
        logging.info("Index created and persisted successfully")
        
        query_engine = index.as_query_engine()
        
        return query_engine
    
    except Exception as e:
        logging.error("Error creating embedding model")
        raise customexception(e, sys)
