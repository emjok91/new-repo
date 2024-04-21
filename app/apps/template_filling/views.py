```python
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import FilledTemplate
from .serializers import FilledTemplateSerializer
from .services import TemplateFillingService

class FilledTemplateViewSet(viewsets.ModelViewSet):
    queryset = FilledTemplate.objects.all()
    serializer_class = FilledTemplateSerializer

    @action(detail=True, methods=['post'])
    def fill_template(self, request, pk=None):
        filled_template = self.get_object()
        template_filling_service = TemplateFillingService()

        try:
            filled_pdf = template_filling_service.fill_template(filled_template)
            filled_template.filled_pdf = filled_pdf
            filled_template.save()

            return Response({'status': 'Template filled successfully'})
        except Exception as e:
            return Response({'status': 'Error filling template', 'message': str(e)}, status=400)
```