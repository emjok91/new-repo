```python
from django.db import models
from app.apps.file_upload.models import UploadedFile
from app.apps.task_extraction.models import ExtractedTask

class FilledTemplate(models.Model):
    file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE, related_name='filled_templates')
    task = models.ForeignKey(ExtractedTask, on_delete=models.CASCADE, related_name='filled_templates')
    filled_pdf = models.FileField(upload_to='filled_templates/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"FilledTemplate {self.id} for File {self.file.id} and Task {self.task.id}"
```