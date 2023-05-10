from explorer_services_api.type_of_service.infrastructure.models import Deliverables
from explorer_services_api.type_of_service.infrastructure.models.package import Package
import pytest

from explorer_services_api.type_of_service.infrastructure.models.type_of_service import TypeOfService

from explorer_services_api.type_of_service.infrastructure.repositories.type_of_service_repository import \
    TypeOfServiceRepository


@pytest.mark.django_db
def test_type_of_service_repository():
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

    type_service_repository = TypeOfServiceRepository()
    type_of_service_by_id = type_service_repository.get_by_id(initial_service.pk)
    assert type_of_service_by_id is not None
    assert type_of_service_by_id.name == 'test'

    type_of_services = type_service_repository.get_all()
    assert len(type_of_services) > 0
    assert type_of_services.get(id=initial_service.pk).name == 'test'
