```python
from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    file = models.FileField(upload_to='uploaded_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Task(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=200)
    task_content = models.TextField()

class Template(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    task_type = models.CharField(max_length=200)
    template_file = models.FileField(upload_to='templates/')

class ProcessedFile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    processed_file = models.FileField(upload_to='processed_files/')
```
