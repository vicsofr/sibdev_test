import csv
from io import TextIOWrapper

from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UploadDealsCsvSerializer(serializers.Serializer):
    deals = serializers.FileField(required=True)

    class Meta:
        fields = ('file',)

    @staticmethod
    def deals_to_list(file: InMemoryUploadedFile) -> list:
        deals_text = TextIOWrapper(file.file, encoding='utf-8')
        csv_list = list(csv.reader(deals_text))
        return csv_list

    def validate_deals(self, deals):
        if deals.name.split('.')[-1] != 'csv':
            raise ValidationError(f'{deals.name} is not a CSV file')

        column_names = {'customer', 'item', 'total', 'quantity', 'date'}
        parsed_deals = self.deals_to_list(deals)

        if column_names != set(parsed_deals[0]):
            raise ValidationError(f'{deals.name} is not a valid CSV file. Column amount or names are different '
                                  f'from template')

        return parsed_deals
