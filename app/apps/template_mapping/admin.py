```python
from django.contrib import admin
from .models import TemplateMapping

class TemplateMappingAdmin(admin.ModelAdmin):
    list_display = ['task_type', 'template_file']
    search_fields = ['task_type', 'template_file']

admin.site.register(TemplateMapping, TemplateMappingAdmin)
```