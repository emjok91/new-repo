```python
from django.test import TestCase
from .models import Task
from .views import extract_tasks

class TaskExtractionTest(TestCase):
    def setUp(self):
        self.task1 = Task.objects.create(name='Prescription', description='Prescribe medication')
        self.task2 = Task.objects.create(name='Referral', description='Refer to specialist')

    def test_task_extraction(self):
        tasks = extract_tasks('Prescribe medication and refer to specialist')
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].name, 'Prescription')
        self.assertEqual(tasks[1].name, 'Referral')

    def test_task_extraction_no_tasks(self):
        tasks = extract_tasks('No tasks here')
        self.assertEqual(len(tasks), 0)
```