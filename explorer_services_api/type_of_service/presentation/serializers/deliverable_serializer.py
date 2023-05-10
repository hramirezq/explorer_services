from rest_framework import serializers


class DeliverableSerializerResponse(serializers.Serializer):
    """

    """
    id = serializers.IntegerField()
    name = serializers.CharField()
