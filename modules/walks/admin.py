from django.contrib import admin
from modules.walks.models import Walk

# Register your models here.

class WalkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Walk, WalkAdmin)    
