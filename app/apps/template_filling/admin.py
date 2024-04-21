```python
from django.contrib import admin
from .models import FilledTemplate

@admin.register(FilledTemplate)
class FilledTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'original_file', 'template', 'filled_file', 'created_at', 'updated_at')
    search_fields = ('original_file', 'template',)
    list_filter = ('created_at', 'updated_at',)
```