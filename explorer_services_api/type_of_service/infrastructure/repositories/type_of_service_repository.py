from explorer_services_api.type_of_service.infrastructure.models import TypeOfService


class TypeOfServiceRepository:

    @staticmethod
    def get_by_id(type_of_service_id):
        """
            This method is used to obtain a service type and its nested objects,
            such as packages and deliverables.

            Args:
                type_of_service_id: Service type identifier.

            Raises:
                TypeOfService.DoesNotExist: When the object does not exist, a none is returned.

        """

        try:
            type_of_service = TypeOfService.objects \
                .prefetch_related('packages', 'packages__deliverables') \
                .get(pk=type_of_service_id)
        except TypeOfService.DoesNotExist:
            return None
        return type_of_service

    @staticmethod
    def get_all():
        """
        This method is used to obtain all types of services
        """
        return TypeOfService.objects \
            .prefetch_related('packages', 'packages__deliverables') \
            .all()
