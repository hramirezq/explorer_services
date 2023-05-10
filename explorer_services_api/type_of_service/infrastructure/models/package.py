from explorer_services_api.type_of_service.infrastructure.models.base_model import BaseModel
from django.db import models


class Package(BaseModel):
    """
    Model of package
    """
    id = models.AutoField(primary_key=True)
    type_of_service_id = models.ForeignKey('TypeOfService', on_delete=models.CASCADE, related_name='packages')
    description = models.CharField('Description', max_length=200, blank=False, null=False)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta(BaseModel.Meta):
        db_table = "packages"
        verbose_name_plural = "Packages"

    def __str__(self):
        return self.description
