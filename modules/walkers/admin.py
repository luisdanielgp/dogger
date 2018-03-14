from django.contrib import admin
from modules.walkers.models import Walker

# Register your models here.

class WalkerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Walker, WalkerAdmin)
