```python
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import FileUpload, ProcessedFile
from .serializers import FileUploadSerializer, ProcessedFileSerializer
from .tasks import process_file

class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer

    def create(self, request, *args, **kwargs):
        file_serializer = FileUploadSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            process_file.delay(file_serializer.instance.id)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProcessedFileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProcessedFile.objects.all()
    serializer_class = ProcessedFileSerializer

    @action(detail=True, methods=['get'])
    def tasks(self, request, pk=None):
        processed_file = self.get_object()
        tasks = processed_file.tasks.all()
        return Response({"tasks": [task.name for task in tasks]})
```
