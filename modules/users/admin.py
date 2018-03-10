from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA
from .models import User
# Register your models here.


class UserAdmin(UA):

    fieldsets = (

        ('Datos de Cuenta', {
            'fields': ('id', 'email', 'password', 'is_active', 'is_staff')
        }),
        ('Datos personales', {
            'fields': ('name', 'lastname_paterno', 'lastname_materno', 'cellphone_num', 'gender')
        }),
        ('Grupos', {
            'fields': ('groups',)
        }),
    )
    # agrega un formulario para poder hashear los passwords
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'groups'),
        }),
    )

    def username(self, instance):
        return instance.email

    def user_first_name(self, instance):
        return instance.name

    def user_last_name(self, instance):
        return instance.lastname_paterno

    list_display = ('email', 'user_first_name', 'user_last_name', 'is_active')
    ordering = ('email',)

class ApplicationAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
