```python
from django.db import models
from app.apps.file_upload.models import UploadedFile
from app.apps.template_filling.models import FilledTemplate

class ProcessedFile(models.Model):
    uploaded_file = models.OneToOneField(UploadedFile, on_delete=models.CASCADE, related_name='processed_file')
    processed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uploaded_file.file_name

class FileResult(models.Model):
    processed_file = models.ForeignKey(ProcessedFile, on_delete=models.CASCADE, related_name='file_results')
    filled_template = models.ForeignKey(FilledTemplate, on_delete=models.CASCADE, related_name='file_results')

    def __str__(self):
        return f'{self.processed_file.file_name} - {self.filled_template.template_name}'
```