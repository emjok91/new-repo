```python
from rest_framework import serializers
from .models import ProcessedFile

class ProcessedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessedFile
        fields = ['file_id', 'task_details', 'template_url']
```