
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
        # queryset = Client.objects.all().values_list('customer', flat=True)
        # queryset = Client.objects.all().values_list('gems', flat=True)
        queryset = Client.objects.all().values('gems')
        serializer = ClientSerializer(queryset, many=True)
        return Response({'data': serializer.data})





    def post(self, request, *args, **kwargs):
        serializer = CSVUploadSerializer(data=request.data)
        if serializer.is_valid():
            csv_file = request.data['csv_file']
            file_obj = csv_file.read().decode('utf-8')
            io_string = io.StringIO(file_obj)
            reader = list(csv.reader(io_string, delimiter=','))

            usernames = []
            for x in reader[1:]:
                usernames.append(x[0])

            names = list(set(usernames))
            obj = []
            for x in names:
                dct = {'username': x}
                for j in reader[1:]:
                    if x == j[0]:
                        try:
                            dct['spent_money'] += int(j[2])
                            dct['gems'] += [j[1]]
                        except KeyError:
                            dct['spent_money'] = int(j[2])
                            dct['gems'] = [j[1]]
                obj.append(dct)

            # for x in obj:
                # print(type(x.get('gems')))


            for x in obj:
                Client.objects.update_or_create(
                    username = x.get('username'),
                    spent_money = x.get('spent_money'),
                    gems = x.get('gems'),
                )

            return Response('OK - файл был обработан без ошибок', status=201)
        else:
            return Response(serializer.errors, status=400)

# filename = Client.objects.last()
# with open('media/' + str(filename), 'r') as f:
#     data = csv.DictReader(f, delimiter=';')
#     print(data.fieldnames)

# serializer = CSVUploadSerializer(filename)
    