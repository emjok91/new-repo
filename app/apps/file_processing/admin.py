```python
from django.contrib import admin
from .models import ProcessedFile

@admin.register(ProcessedFile)
class ProcessedFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'status', 'processed_at')
    search_fields = ('id', 'file')
    list_filter = ('status',)
```