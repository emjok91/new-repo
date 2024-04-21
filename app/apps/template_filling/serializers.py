```python
from rest_framework import serializers
from .models import FilledTemplate

class FilledTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilledTemplate
        fields = ['id', 'original_file', 'template', 'filled_template', 'created_at', 'updated_at']
```