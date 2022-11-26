from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import converter_csv_to_json
# Create your views here.

class GetJson(APIView):
    def get(self, req):
        data = converter_csv_to_json('data.csv')
        return Response(data, status=status.HTTP_200_OK)
