```python
from rest_framework.views import exception_handler
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

        # Log the error
        logger.error(f"Error occurred: {exc}, Status Code: {response.status_code}")

    return response

class ErrorLogView(APIView):
    def get(self, request, format=None):
        logs = []
        with open('error.log', 'r') as file:
            for line in file:
                logs.append(line)
        return Response({"logs": logs})
```