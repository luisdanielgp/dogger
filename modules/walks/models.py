from django.db import models
from modules.walkers.models import Walker
from modules.owners.models import Owner
from modules.dogs.models import Dog
from modules.hours.models import Hour
import uuid

# Create your models here.

class Walk(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    walker = models.ForeignKey(Walker, on_delete=models.CASCADE, related_name="walk")
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="walk")
    dog = models.ManyToManyField(Dog, related_name="walk")
    place = models.IntegerField(default=3)
    hour = models.ForeignKey(Hour, on_delete=models.CASCADE, related_name="walk")

    def __int__(self):
        return self.id

    def __unicode__(self):
        return
