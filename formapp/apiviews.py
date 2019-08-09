from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Amarform


class AmarformView(APIView):
    def get(self, request):
        amarform = Amarform.objects.all()
        return Response({"amarform": amarform})