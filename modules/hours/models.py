from django.db import models
import uuid

# Create your models here.

class Hour(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=10)
    hour = models.IntegerField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return
