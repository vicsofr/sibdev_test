from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from deals.models import Deal
from deals.serializers.upload_deals_csv import UploadDealsCsvSerializer
from deals.utils import deals_to_model


class UploadDealsCsvView(CreateAPIView, CreateModelMixin):
    serializer_class = UploadDealsCsvSerializer
    http_allowed_methods = ['POST']
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        """
        POST method /deals/upload_deals_csv.
        Uploads csv-file with all
        """
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response({"result": "error", "error": serializer.errors})

        deals_list = serializer.validated_data.pop('deals')
        deals_for_insert = deals_to_model(deals_list)

        Deal.objects.all().delete()
        Deal.objects.bulk_create(deals_for_insert)

        return Response(
            {
                'status': 'OK',
                'inserted': len(deals_for_insert)
            }
        )
