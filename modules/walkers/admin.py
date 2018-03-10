from django.contrib import admin
from modules.walkers.models import Walker, Hour_available, Walk

# Register your models here.

class WalkerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Walker, WalkerAdmin)

class Hour_availableAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hour_available, Hour_availableAdmin)

class WalkAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Walk, WalkAdmin)
