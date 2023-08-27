from rest_framework import serializers
from . models import Client

class ClientSerializer(serializers.ModelSerializer):

    class Meta:

        model = Client
        fields = ('customer', 'item', 'total')
        # fields = '__all__'


class CSVUploadSerializer(serializers.Serializer):

    csv_file = serializers.FileField()
