from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Amarform
from .serializers import AmarformSerializer

class AmarformView(APIView):
    def get(self, request):
        amarform = Amarform.objects.all()
        amarform_serializer = AmarformSerializer(amarform, many = True)
        return Response(amarform_serializer.data)
        # return Response({'amarform':amarform})

class AmarformDetailView(APIView):
    def get(self, request, id):
        amarform = Amarform.objects.get(id = id)
        amarform_serializer = AmarformSerializer(amarform)
        return Response(amarform_serializer.data)   

class AmarformUpdateView(APIView):
    def get(self, request, id):
        amarform = Amarform.objects.get(id = id)
        amarform_serializer = AmarformSerializer(amarform)
        return Response(amarform_serializer.data)         