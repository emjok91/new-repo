```python
from django.contrib import admin
from .models import ErrorLog

@admin.register(ErrorLog)
class ErrorLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'error_type', 'file_id', 'message')
    search_fields = ('error_type', 'file_id')
    list_filter = ('timestamp', 'error_type')
```