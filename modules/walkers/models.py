from django.db import models
from modules.users.models import User
from modules.hours.models import Hour
import uuid

# Create your models here.

class Walker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="walker")
    hour = models.ManyToManyField(Hour, related_name="walker")

    def __str__(self):
        return self.user.name

    def __unicode__(self):
        return
