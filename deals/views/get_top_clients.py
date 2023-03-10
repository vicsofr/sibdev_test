from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Sum, F
from django.core.cache import cache

from deals.models import Deal
from deals.serializers.get_top_clients import GetTopClientsSerializer
from deals.utils import gems_by_two_more_clients


class GetTopClientsView(APIView):
    serializer_class = GetTopClientsSerializer
    http_allowed_methods = ['GET']
    permission_classes = (permissions.AllowAny,)

    @staticmethod
    def get_queryset():
        """Get queryset of 5 clients with the largest sum of 'total' and list of a gems they bought"""
        top_5 = Deal.objects.filter(
            last_parse=True
        ).values(
            'customer'
        ).annotate(
            username=F('customer'),
            spent_money=Sum('total'),
            gems=ArrayAgg('item', distinct=True)
        ).order_by(
            '-spent_money',
        )
        return top_5[:5]

    def get(self, request):
        """
        GET method /deals/get_top_clients
        When called shows information about 5 users with the largest sum of 'total' and list of a gems that been bought
        by them and at least one other client
        """
        response = cache.get('top_clients')

        if not response:
            queryset = self.get_queryset()
            if not queryset:
                return Response(
                    {
                        "status": "error",
                        "description": "No data about clients deals. Use POST /post_deals_csv to upload data"
                    }
                )

            serialized_data = self.serializer_class(queryset, many=True).data
            serialized_gems_list = [client['gems'] for client in serialized_data]

            changed_gems_list = gems_by_two_more_clients(serialized_gems_list)

            for number, client in enumerate(serialized_data):
                client['gems'] = changed_gems_list[number]

            response = serialized_data
            cache.set('top_clients', response)

        return Response(
            {
                "response": response,
            }
        )
