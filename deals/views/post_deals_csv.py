from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from deals.models import Deal
from deals.serializers.post_deals_csv import UploadDealsCsvSerializer
from deals.utils import deals_to_model


class UploadDealsCsvView(APIView):
    serializer_class = UploadDealsCsvSerializer
    http_allowed_methods = ('POST',)
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        """
        POST method /deals/upload_deals_csv.
        When called uploads attached csv-file data in deals table and setting 'last_parse' = False to previous uploads
        """
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(
                {
                    "status": "error",
                    "description": serializer.errors
                }
            )

        deals_list = serializer.validated_data.pop('deals')
        deals_for_insert = deals_to_model(deals_list)

        Deal.objects.all().update(last_parse=False)
        Deal.objects.bulk_create(deals_for_insert)

        return Response(
            {
                'status': 'OK',
                'inserted': len(deals_for_insert)
            }
        )
