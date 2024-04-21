```python
from django.test import TestCase
from .models import ProcessedFile
from .views import process_file
from django.core.files.uploadedfile import SimpleUploadedFile
import os

class FileProcessingTest(TestCase):

    def setUp(self):
        self.test_file = SimpleUploadedFile(
            name='test.pdf',
            content=open('path/to/test.pdf', 'rb').read(),
            content_type='application/pdf'
        )
        self.processed_file = ProcessedFile.objects.create(file=self.test_file)

    def tearDown(self):
        os.remove(self.processed_file.file.path)

    def test_file_processing(self):
        response = process_file(self.processed_file.id)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.processed_file.is_processed)
        self.assertIsNotNone(self.processed_file.processed_text)
```
