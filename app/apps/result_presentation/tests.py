```python
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import ProcessedFile

class ResultPresentationTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_retrieve_processed_files(self):
        # Create some test processed files
        ProcessedFile.objects.create(file_id='file1', task_details='task1', template_url='url1')
        ProcessedFile.objects.create(file_id='file2', task_details='task2', template_url='url2')

        # Get the list of processed files
        response = self.client.get(reverse('processedfile-list'))

        # Check the status code and the length of the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_processed_file(self):
        # Create a test processed file
        processed_file = ProcessedFile.objects.create(file_id='file1', task_details='task1', template_url='url1')

        # Get the processed file
        response = self.client.get(reverse('processedfile-detail', args=[processed_file.id]))

        # Check the status code and the response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['file_id'], 'file1')
        self.assertEqual(response.data['task_details'], 'task1')
        self.assertEqual(response.data['template_url'], 'url1')
```