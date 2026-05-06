from llama_index.core import SimpleDirectoryReader
import sys
from logger import logging
from exception import customexception

def load_data_from_directory(data):
    try :
        logging.info("Loading data from directory")
        loader = SimpleDirectoryReader(data)
        documents = loader.load_data()
        logging.info("Data loaded successfully from directory")
        return documents
    except Exception as e:
        logging.error("Error occurred while loading data from directory")
        raise customexception(e, sys)