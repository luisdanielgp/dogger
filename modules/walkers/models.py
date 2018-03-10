from django.db import models
from modules.users.models import User

# Create your models here.

class Walker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="walker")

    def __unicode__(self):
        return

# Hours available for every walker

class Hour_available(models.Model):
    hour = models.IntegerField()
    walkers = models.ManyToManyField(Walker, blank=True)

    def __unicode__(self):
        return

class Walk(models.Model):
    walker = models.ForeignKey(Walker, on_delete=models.CASCADE, related_name="walk")
    start = models.OneToOneField(Hour_available, on_delete=models.CASCADE, related_name="start")
    end = models.OneToOneField(Hour_available, on_delete=models.CASCADE, related_name="end")
