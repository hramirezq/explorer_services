from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from explorer_services_api.type_of_service.application.use_cases.get_type_of_service_by_id_use_case import \
    GetTypeOfServiceByIdUseCase
from explorer_services_api.type_of_service.application.use_cases.get_type_of_services_use_case import GetTypeOfServicesUseCase
from explorer_services_api.type_of_service.presentation.serializers.type_of_service_serializer import \
    TypeOfServiceSerializerResponse


class TypeOfServiceViewSets(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):

    def list(self, request, *args, **kwargs):
        queryset = GetTypeOfServicesUseCase().run()
        serializer = TypeOfServiceSerializerResponse(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = GetTypeOfServiceByIdUseCase().run(kwargs.get('pk'))
        if instance is None:
            return Response("El tipo de servicio no existe", status.HTTP_400_BAD_REQUEST)
        serializer = TypeOfServiceSerializerResponse(instance)
        return Response(serializer.data)
