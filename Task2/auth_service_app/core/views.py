from rest_framework import response, status
from rest_framework.views import APIView


class HealthCheckView(APIView):

    def get(self, request):
        return response.Response(
            {"Health Check": "OK"}, status=status.HTTP_200_OK)
