from explorer_services_api.type_of_service.infrastructure.models.base_model import BaseModel
from django.db import models


class Deliverables(BaseModel):
    """
    Model of derivable
    """
    id = models.AutoField(primary_key=True)
    package_Id = models.ForeignKey('Package', on_delete=models.CASCADE, related_name='deliverables')
    name = models.CharField('Name', max_length=200, blank=False, null=False)

    class Meta(BaseModel.Meta):
        db_table = "deliverables"
        verbose_name_plural = "Deliverables"

    def __str__(self):
        return self.name
