```python
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import TemplateMapping
from .serializers import TemplateMappingSerializer

class TemplateMappingViewSet(viewsets.ModelViewSet):
    queryset = TemplateMapping.objects.all()
    serializer_class = TemplateMappingSerializer

    @action(detail=True, methods=['post'])
    def map_template(self, request, pk=None):
        template_mapping = self.get_object()
        task = request.data.get('task')

        if not task:
            return Response({'error': 'Task is required to map a template.'}, status=400)

        try:
            template_mapping.map_task_to_template(task)
            return Response({'message': 'Template successfully mapped.'})
        except Exception as e:
            return Response({'error': str(e)}, status=500)
```