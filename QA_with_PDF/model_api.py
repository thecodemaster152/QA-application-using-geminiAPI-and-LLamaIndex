import os
from dotenv import load_dotenv
import sys

from llama_index.llms.gemini import Gemini
from IPython.display import Markdown, display
import google.generativeai as genai
from exception import customexception
from logger import logging

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
    try:
        model = Gemini(
            model="models/gemma-4-26b-a4b-it",
            api_key=GOOGLE_API_KEY
        )
        logging.info("Model loaded successfully")
        return model
    except Exception as e:
        logging.error("Error loading model")
        raise customexception(e, sys)