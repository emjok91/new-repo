```python
from django.test import TestCase
from .models import TemplateFilling
from .views import fill_template

class TemplateFillingTestCase(TestCase):
    def setUp(self):
        TemplateFilling.objects.create(task_id="1", template_path="templates/template1.pdf", filled_template_path="filled_templates/filled_template1.pdf")

    def test_template_filling(self):
        template_filling1 = TemplateFilling.objects.get(task_id="1")
        self.assertEqual(template_filling1.template_path, "templates/template1.pdf")
        self.assertEqual(template_filling1.filled_template_path, "filled_templates/filled_template1.pdf")

    def test_fill_template(self):
        response = fill_template("1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['task_id'], "1")
        self.assertEqual(response.data['template_path'], "templates/template1.pdf")
        self.assertEqual(response.data['filled_template_path'], "filled_templates/filled_template1.pdf")
```