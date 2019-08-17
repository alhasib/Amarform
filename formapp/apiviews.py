from rest_framework.response import Response
from rest_framework.views import APIView
import json 
from .models import Amarform
from .serializers import AmarformSerializer

# this is a list view
class AmarformView(APIView):
    def get(self, request):
        amarform = Amarform.objects.all()
        amarform_serializer = AmarformSerializer(amarform, many = True)
        return Response(amarform_serializer.data)


# this is detail view with get and post request
class AmarformDetailView(APIView):
    def get(self, request, pk):   #get method()
        print("get")
        amarform = Amarform.objects.get(pk = pk)
        amarform_serializer = AmarformSerializer(amarform)
        return Response(amarform_serializer.data)   

    def post(self, request, pk, format=None): #post method()
        print('post')
        a = Amarform.objects.get(pk = pk)
        data = request.data
        data_type = type(data)
        
       
        if data_type is dict:
           
            amarform_serializer = AmarformSerializer(a, data = data)
            if amarform_serializer.is_valid():
                print('sabu')
                amarform_serializer.save()
                return Response(amarform_serializer.data)


            else:
                
                return Response(amarform_serializer.errors)
            amarform = Amarform.objects.get()
            amarform_serializer = AmarformSerializer(amarform)

        else:
            a.user_info["username"] = data['user_info[username]']
            a.user_info["first_name"] = data['user_info[first_name]']
            a.user_info["last_name"] = data['user_info[last_name]']
            a.mobile_number = data['mobile_number']
            a.professional_info["company"] = data['professional_info[company]']
            a.professional_info["salary"] = data['professional_info[salary]']
            a.save()    
        return Response({"status":"success"})             



