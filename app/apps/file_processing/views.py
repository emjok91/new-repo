```python
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ProcessedFile
from .serializers import ProcessedFileSerializer
from .tasks import process_file

class FileProcessingView(APIView):
    def post(self, request, *args, **kwargs):
        file_serializer = ProcessedFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            process_file.delay(file_serializer.instance.id)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        files = ProcessedFile.objects.all()
        serializer = ProcessedFileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
```