```python
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'task_type', 'task_details', 'created_at', 'updated_at')
    search_fields = ('task_type', 'task_details')
    list_filter = ('task_type',)
```