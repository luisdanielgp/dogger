from django.db import models
from modules.users.models import User
import uuid

# Create your models here.

class Owner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="owner")

    def __str__(self):
        return self.user.name

    def __unicode__(self):
        return
