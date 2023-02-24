from rest_framework import serializers


class GetTopClientsSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    spent_money = serializers.IntegerField(required=True)
    gems = serializers.ListSerializer(child=serializers.CharField(), required=True)
