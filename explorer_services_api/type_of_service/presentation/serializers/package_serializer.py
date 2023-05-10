from rest_framework import serializers

from explorer_services_api.type_of_service.presentation.serializers.deliverable_serializer import \
    DeliverableSerializerResponse


class PackageSerializerResponse(serializers.Serializer):
    """

    """
    id = serializers.IntegerField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=19, decimal_places=2)
    typeOfServiceID = serializers.PrimaryKeyRelatedField(read_only=True)
    deliverables = DeliverableSerializerResponse(many=True, read_only=True)
