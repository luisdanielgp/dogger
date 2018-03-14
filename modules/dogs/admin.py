from django.contrib import admin
from modules.dogs.models import Dog

# Register your models here.

class DogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dog, DogAdmin)
