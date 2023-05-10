from explorer_services_api.type_of_service.infrastructure.repositories.type_of_service_repository import \
    TypeOfServiceRepository


class GetTypeOfServiceByIdUseCase:
    type_service_repository = TypeOfServiceRepository()

    @classmethod
    def run(cls, type_of_service_id):
        users = cls.process(type_of_service_id)
        return users

    @classmethod
    def process(cls, type_of_service_id):
        return cls.type_service_repository.get_by_id(type_of_service_id)
