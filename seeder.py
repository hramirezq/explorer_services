import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "explorer_services_api.settings")
import django


django.setup()



from explorer_services_api.type_of_service.infrastructure.models import TypeOfService, Package, Deliverables


def seed_data():
    # Crea un tipo de servicio
    type_service = TypeOfService.objects.create(
        name='Desarrollos On-Cloud',
    )
    type_service.save()

    # Crea un paquete relacionado al tipo de servicio
    package = Package.objects.create(
        type_of_service_id=type_service,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing eli",
        price=100,
    )
    package.save()

    # Crea un entregable relacionado con el paquete
    deliverable = Deliverables.objects.create(
        package_Id=package,
        name="Include source code",
    )
    deliverable.save()

    type_service_two = TypeOfService.objects.create(
        name='Development of solutions',
    )
    type_service_two.save()

    package_two = Package.objects.create(
        type_of_service_id=type_service_two,
        description="Lorem ipsum dolor sit amet, consectetur",
        price=100,
    )
    package_two.save()

    deliverable_two = Deliverables.objects.create(
        package_Id=package_two,
        name="Include source code",
    )
    deliverable_two.save()


if __name__ == "__main__":
    print("Creando datos")
    seed_data()
