from rest_framework import serializers
from . models import Client

class CSVUploaderializer(serializers.Serializer):

    csv_file = serializers.FileField()