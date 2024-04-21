```python
from django.test import TestCase
from .models import ErrorLog

class ErrorLogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        ErrorLog.objects.create(
            file_id='1234',
            error_message='Test error message',
            error_type='File Upload',
            error_timestamp='2022-01-01T00:00:00Z'
        )

    def test_error_message_content(self):
        error_log = ErrorLog.objects.get(id=1)
        expected_error_message = f'{error_log.error_message}'
        self.assertEqual(expected_error_message, 'Test error message')

    def test_error_type_content(self):
        error_log = ErrorLog.objects.get(id=1)
        expected_error_type = f'{error_log.error_type}'
        self.assertEqual(expected_error_type, 'File Upload')

    def test_error_timestamp_content(self):
        error_log = ErrorLog.objects.get(id=1)
        expected_error_timestamp = f'{error_log.error_timestamp}'
        self.assertEqual(expected_error_timestamp, '2022-01-01T00:00:00Z')
```