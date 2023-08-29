
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
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response({'data': serializer.data})

    def post(self, request, *args, **kwargs):
        serializer = CSVUploadSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('OK - файл был обработан без ошибок', status=201)
            # return Response('OK - файл был обработан без ошибок', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)
