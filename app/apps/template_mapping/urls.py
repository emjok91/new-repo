```python
from django.urls import path
from . import views

app_name = 'template_mapping'

urlpatterns = [
    path('map/', views.TemplateMappingView.as_view(), name='map'),
]
```