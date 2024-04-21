```python
from celery import shared_task
from .models import FileUpload, Task
from .utils import extract_text_from_pdf, preprocess_text, extract_tasks, map_templates, fill_templates
import os
import spacy

@shared_task
def process_file(file_id):
    try:
        file = FileUpload.objects.get(id=file_id)
        file_path = file.file.path

        # Extract text from PDF
        text = extract_text_from_pdf(file_path)

        # Preprocess text
        preprocessed_text = preprocess_text(text)

        # Load spaCy model
        nlp = spacy.load("en_core_sci_sm")

        # Extract tasks
        tasks = extract_tasks(nlp, preprocessed_text)

        # Map tasks to templates
        mapped_tasks = map_templates(tasks)

        # Fill templates
        filled_templates = fill_templates(mapped_tasks)

        # Save tasks to database
        for task in filled_templates:
            Task.objects.create(file=file, task_type=task['type'], content=task['content'])

        # Update file status
        file.status = 'Processed'
        file.save()

    except Exception as e:
        # Log error and update file status
        print(f"Error processing file {file_id}: {str(e)}")
        file.status = 'Error'
        file.save()
```
