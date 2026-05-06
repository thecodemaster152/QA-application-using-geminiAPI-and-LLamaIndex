import logging
import os
from pathlib import Path

list_of_files = [
    "QA_with_PDF/__init__.py",
    "QA_with_PDF/data_ingestion.py",
    "QA_with_PDF/embedding.py",
    "QA_with_PDF/model_api.py",
    "Experiments/experiment.ipynb",
    "StreamlitApp.py",
    "logger.py",
    "execution.py",
    "setup.py"
    ]     


for filepath in list_of_files:
    path = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory '{filedir}' created successfully.")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"File '{filename}' created successfully.")

    else:
        logging.info(f"File '{filename}' already exists and is not empty.") 