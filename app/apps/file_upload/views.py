```python
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UploadedFile
from .serializers import FileUploadSerializer
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import uuid
import os

class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        file_serializer = FileUploadSerializer(data=request.data)

        if file_serializer.is_valid():
            file = request.data['file']
            file_extension = os.path.splitext(file.name)[1]
            if file_extension != '.pdf':
                return Response({"error": "Invalid file type. Only PDF files are allowed."}, status=status.HTTP_400_BAD_REQUEST)

            unique_filename = str(uuid.uuid4()) + file_extension
            file_save_path = 'uploads/' + unique_filename
            default_storage.save(file_save_path, ContentFile(file.read()))

            uploaded_file = UploadedFile.objects.create(file=file_save_path)
            return Response({"message": "File uploaded successfully.", "file_id": uploaded_file.id}, status=status.HTTP_201_CREATED)

        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```