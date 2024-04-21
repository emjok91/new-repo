```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/file_upload/', include('app.apps.file_upload.urls')),
    path('api/file_processing/', include('app.apps.file_processing.urls')),
    path('api/task_extraction/', include('app.apps.task_extraction.urls')),
    path('api/template_mapping/', include('app.apps.template_mapping.urls')),
    path('api/template_filling/', include('app.apps.template_filling.urls')),
    path('api/result_presentation/', include('app.apps.result_presentation.urls')),
    path('api/error_handling/', include('app.apps.error_handling.urls')),
]
```