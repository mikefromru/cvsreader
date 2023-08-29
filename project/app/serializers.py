from rest_framework import serializers
from . models import Client
from django.core.validators import FileExtensionValidator
import os
import csv
import io


class ClientSerializer(serializers.ModelSerializer):

    class Meta:

        model = Client
        fields = '__all__'


class CSVUploadSerializer(serializers.Serializer):

    csv_file = serializers.FileField(
        max_length=30,
        validators=[FileExtensionValidator(allowed_extensions=['csv'])],
        allow_empty_file=False,
    )

    def create(self, validated_data):
        csv_file = self.context['request'].data['csv_file']
        file_obj = csv_file.read().decode('utf-8')
        io_string = io.StringIO(file_obj)
        reader = list(csv.reader(io_string, delimiter=','))

        # get only cusomers 
        customers = [x[0] for x in reader[1:]] 

        obj = []
        for customer in list(set(customers)):
            dct = {'username': customer}
            for row in reader[1:]:
                if customer == row[0]:
                    try:
                        dct['spent_money'] += int(row[2])
                        dct['gems'] += [row[1]]
                    except KeyError:
                        dct['spent_money'] = int(row[2])
                        dct['gems'] = [row[1]]
            obj.append(dct)

        # for x in obj:
        #     deals = Client.objects.update_or_create(
        #         username = x.get('username'),
        #         spent_money = x.get('spent_money'),
        #         gems = x.get('gems'),
        #     )

        obj_list = [Client(**data_dict) for data_dict in obj]
        return Client.objects.bulk_create(
            obj_list,
              update_conflicts=False,
              unique_fields=['username'],
              update_fields=['spent_money', 'gems'],
            )