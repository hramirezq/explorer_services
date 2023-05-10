from django.db import models


class BaseModel(models.Model):
    """
    Base model ..
    """
    objects: models.Manager()
    DoesNotExist: models.ObjectDoesNotExist

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created',
        null=True
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified',
        null=True
    )

    class Meta:
        """Meta option."""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
