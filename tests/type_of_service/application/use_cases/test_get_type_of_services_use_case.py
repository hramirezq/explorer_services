from explorer_services_api.type_of_service.application.use_cases.get_type_of_services_use_case import \
    GetTypeOfServicesUseCase
from explorer_services_api.type_of_service.infrastructure.models import Deliverables
from explorer_services_api.type_of_service.infrastructure.models.package import Package
import pytest

from explorer_services_api.type_of_service.infrastructure.models.type_of_service import TypeOfService


@pytest.mark.django_db
def test_get_type_of_services_use_case():
    initial_service = TypeOfService.objects.create(name='test')
    initial_service.save()

    initial_package = Package.objects.create(
        type_of_service_id=initial_service,
        description='test package',
        price=100
    )
    initial_package.save()

    initial_deliverable = Deliverables.objects.create(
        package_Id=initial_package,
        name='test deliverable'
    )
    initial_deliverable.save()

    type_of_services = GetTypeOfServicesUseCase().run()
    assert len(type_of_services) > 0
    assert type_of_services.get(id=initial_service.pk).name == 'test'
    assert type_of_services.get(id=initial_service.pk)\
               .packages.get(id=initial_package.pk).description == 'test package'
    assert type_of_services.get(id=initial_service.pk)\
               .packages.get(id=initial_package.pk)\
               .deliverables.get(id=initial_deliverable.pk).name == 'test deliverable'
