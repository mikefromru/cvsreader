
from project.settings import BASE_DIR
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from . models import Client

from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from . serializers import CSVUploadSerializer, ClientSerializer
import csv
import io


class ClientView(APIView):

    parser_classes = (MultiPartParser, FormParser, JSONParser)
    serializer_class =  CSVUploadSerializer




    def get(self, request):
        queryset = Client.objects.filter(total=612).values('customer', 'item', 'total')
        # var = queryset.values_list('customer', 'item').values_list()
        # print(var)
        serializer = ClientSerializer(queryset, many=True)
        return Response({'data': serializer.data})





    def post(self, request, *args, **kwargs):
        serializer = CSVUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer = CSVUploadSerializer(data=request.data)
            if serializer.is_valid():
                csv_file = request.data['csv_file']
                file_obj = csv_file.read().decode('utf-8')
                io_string = io.StringIO(file_obj)
                reader = list(csv.reader(io_string, delimiter=','))

                for x in reader[1:]:

                    Client.objects.update_or_create(
                        customer = x[0],
                        item = x[1],
                        total = x[2],
                        quantity = x[3],
                        date = x[4],
                    )

                return Response('OK - файл был обработан без ошибок', status=201)
            else:
                return Response(serializer.errors, status=400)

# filename = Client.objects.last()
# with open('media/' + str(filename), 'r') as f:
#     data = csv.DictReader(f, delimiter=';')
#     print(data.fieldnames)

# serializer = CSVUploadSerializer(filename)
    