from rest_framework import serializers

from explorer_services_api.type_of_service.presentation.serializers.package_serializer import PackageSerializerResponse


class TypeOfServiceSerializerResponse(serializers.Serializer):
    """

    """
    id = serializers.IntegerField()
    name = serializers.CharField()
    packages = PackageSerializerResponse(many=True, read_only=True)
