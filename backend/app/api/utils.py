```python
import os
import re
from PyPDF2 import PdfFileReader
from pdfminer.high_level import extract_text
import spacy

def validate_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PdfFileReader(file)
            if reader.isEncrypted:
                return False
            return True
    except:
        return False

def extract_text_from_pdf(file_path):
    try:
        text = extract_text(file_path)
        return text
    except:
        return None

def preprocess_text(text):
    text = re.sub(r'\n', ' ', text)  # replace newline characters with space
    text = re.sub(r'\s+', ' ', text)  # replace multiple spaces with single space
    return text

def extract_tasks(text):
    nlp = spacy.load("en_core_sci_sm")
    doc = nlp(text)
    tasks = []
    for ent in doc.ents:
        tasks.append(ent.text)
    return tasks
```