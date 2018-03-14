from django.contrib import admin
from modules.owners.models import Owner

# Register your models here.

class OwnerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Owner, OwnerAdmin)
