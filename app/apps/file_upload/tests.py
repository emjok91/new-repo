```python
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import UploadedFile

class FileUploadTestCase(TestCase):
    def setUp(self):
        self.file = SimpleUploadedFile("file.pdf", b"file_content", content_type="application/pdf")

    def test_file_upload(self):
        uploaded_file = UploadedFile(file=self.file)
        uploaded_file.save()

        self.assertEqual(UploadedFile.objects.count(), 1)
        self.assertEqual(UploadedFile.objects.get().file.name, self.file.name)
        self.assertEqual(UploadedFile.objects.get().file.size, self.file.size)

    def test_file_validation(self):
        invalid_file = SimpleUploadedFile("file.txt", b"file_content", content_type="text/plain")
        with self.assertRaises(Exception):
            UploadedFile(file=invalid_file).save()

    def test_unique_identifier(self):
        uploaded_file1 = UploadedFile(file=self.file)
        uploaded_file1.save()
        uploaded_file2 = UploadedFile(file=self.file)
        uploaded_file2.save()

        self.assertNotEqual(uploaded_file1.id, uploaded_file2.id)
```