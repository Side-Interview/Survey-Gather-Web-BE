from django.db import models
from django.utils import timezone


# Create your models here.
class CreateAtUpdateAt(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
