```python
from django.urls import path
from .api import views

urlpatterns = [
    path('upload/', views.FileUploadView.as_view(), name='file_upload'),
    path('files/', views.FileListView.as_view(), name='file_list'),
    path('files/<int:pk>/', views.FileDetailView.as_view(), name='file_detail'),
    path('templates/', views.TemplateListView.as_view(), name='template_list'),
    path('templates/<int:pk>/', views.TemplateDetailView.as_view(), name='template_detail'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
]
```