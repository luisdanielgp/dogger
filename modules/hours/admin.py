from django.contrib import admin
from modules.hours.models import Hour

# Register your models here.

class HourAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name': ('hour',)}

admin.site.register(Hour, HourAdmin)
