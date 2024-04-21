```python
from django.db import models
from app.apps.task_extraction.models import Task

class Template(models.Model):
    name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)

class TaskTemplateMapping(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
```