```python
from django.db import models
from django.core.validators import FileExtensionValidator

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploaded_files/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return str(self.unique_id)
```