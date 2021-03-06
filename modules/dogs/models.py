from django.db import models
from modules.owners.models import Owner
import uuid

# Create your models here.

class Dog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="dog")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return
