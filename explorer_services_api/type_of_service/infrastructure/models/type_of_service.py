from explorer_services_api.type_of_service.infrastructure.models.base_model import BaseModel
from django.db import models


class TypeOfService(BaseModel):
    """
    Model of type of service
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=150, blank=False, null=False)

    class Meta(BaseModel.Meta):
        db_table = "type_of_services"
        verbose_name_plural = "Type of services"

    def __str__(self):
        return self.name
