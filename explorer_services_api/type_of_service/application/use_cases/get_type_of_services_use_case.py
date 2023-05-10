from explorer_services_api.type_of_service.infrastructure.repositories.type_of_service_repository import \
    TypeOfServiceRepository


class GetTypeOfServicesUseCase:
    type_service_repository = TypeOfServiceRepository()

    @classmethod
    def run(cls):
        data = cls.process()
        return data

    @classmethod
    def process(cls):
        return cls.type_service_repository.get_all()

