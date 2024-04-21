```python
from django.test import TestCase
from .models import TemplateMapping
from .views import map_template

class TemplateMappingTestCase(TestCase):
    def setUp(self):
        TemplateMapping.objects.create(task="prescription", template="prescription_template.pdf")
        TemplateMapping.objects.create(task="referral", template="referral_template.pdf")

    def test_template_mapping(self):
        prescription = TemplateMapping.objects.get(task="prescription")
        referral = TemplateMapping.objects.get(task="referral")

        self.assertEqual(prescription.template, 'prescription_template.pdf')
        self.assertEqual(referral.template, 'referral_template.pdf')

    def test_map_template(self):
        prescription = TemplateMapping.objects.get(task="prescription")
        referral = TemplateMapping.objects.get(task="referral")

        self.assertEqual(map_template("prescription"), prescription.template)
        self.assertEqual(map_template("referral"), referral.template)
```