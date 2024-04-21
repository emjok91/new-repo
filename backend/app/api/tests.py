```python
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import File, Task, Template
from .serializers import FileSerializer, TaskSerializer, TemplateSerializer

class FileUploadTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_file_upload(self):
        with open('test.pdf', 'rb') as file:
            response = self.client.post(reverse('file-upload'), {'file': file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class FileProcessingTestCase(TestCase):
    def setUp(self):
        self.file = File.objects.create(file='test.pdf')

    def test_file_processing(self):
        response = self.client.get(reverse('file-processing', kwargs={'pk': self.file.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TaskExtractionTestCase(TestCase):
    def setUp(self):
        self.file = File.objects.create(file='test.pdf')

    def test_task_extraction(self):
        response = self.client.get(reverse('task-extraction', kwargs={'pk': self.file.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TemplateMappingTestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(name='test task', file=self.file)

    def test_template_mapping(self):
        response = self.client.get(reverse('template-mapping', kwargs={'pk': self.task.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TemplateFillingTestCase(TestCase):
    def setUp(self):
        self.template = Template.objects.create(name='test template', task=self.task)

    def test_template_filling(self):
        response = self.client.get(reverse('template-filling', kwargs={'pk': self.template.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ResultPresentationTestCase(TestCase):
    def test_result_presentation(self):
        response = self.client.get(reverse('result-presentation'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
```