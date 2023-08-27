
from project.settings import BASE_DIR
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from . models import Client

from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from . serializers import CSVUploaderializer
import csv



class FooView(APIView):

    parser_classes = (MultiPartParser, FormParser, JSONParser)
    serializer_class =  CSVUploaderializer

    def get(self, request):

        filename = Client.objects.last()
        with open('media/' + str(filename), 'r') as f:
            data = csv.DictReader(f, delimiter=';')
            print(data.fieldnames)
        
        serializer = CSVUploaderializer(filename)
            
        return Response({'data': serializer.data})
    
    def post(self, request, *args, **kwargs):
        import io
        serializer = CSVUploaderializer(data=request.data)
        if serializer.is_valid():
            csv_file = request.data['csv_file']

            file_obj = csv_file.read().decode('utf-8')
            io_string = io.StringIO(file_obj)
            reader = list(csv.reader(io_string, delimiter=','))
            for x in reader[1:]:
                Client.objects.create(
                    customer = x[0],
                    item = x[1],
                    total = x[2],
                    quantity = x[3],
                    date = x[4]
                )


            '''
            serializer.save()
            filename = serializer.data['file'].strip('/')            
            with open(BASE_DIR / filename, 'r') as f:
                rows = list(csv.reader(f, delimiter=','))                
                for x in rows[1:]:
                    Client(
                        username = x[0],
                        item = x[1],
                    ).save()
            '''

            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
