from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from . serializers import UploadFileSerializer
from . models import File 
import csv

class FooView(APIView):

    parser_classes = (MultiPartParser, FormParser, JSONParser)
    serializer_class =  UploadFileSerializer

    def get(self, request):

        filename = File.objects.last()
        with open('media/' + str(filename), 'r') as f:
            data = csv.DictReader(f, delimiter=';')
            print(data.fieldnames)
        
        serializer = UploadFileSerializer(filename)
            
        return Response({'data': serializer.data})
    
    def post(self, request, *args, **kwargs):
        serializer = UploadFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
        

        # serializer = UploadFileSerializer(data=request.data, orequest.FILES)
        # print(serializer.data)

        # file_obj = request.FILES['upload_file']
        # print(file_obj)


        # with open(var, 'r', encoding='utf-8') as f:
        # data = csv.DictReader(var, delimiter=';')
        # print(data.fieldnames)
            # print(', '.join(x))


