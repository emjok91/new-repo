```python
from django.urls import path
from . import views

urlpatterns = [
    path('extract-tasks/', views.extract_tasks, name='extract_tasks'),
]
```