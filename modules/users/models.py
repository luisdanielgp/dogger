from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
import uuid
# Create your models here.


class UserManager(BaseUserManager, models.Manager):
    def _create_user(self, email, password,
                     is_active, is_superuser, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_active=is_active,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(
            email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(
            email, password, True, True, is_staff=True, ** extra_fields)


class User(AbstractBaseUser, PermissionsMixin, models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=True, default=uuid.uuid4)
    name = models.CharField(max_length=40)
    lastname_paterno = models.CharField(max_length=40)
    lastname_materno = models.CharField(max_length=40)
    cellphone_num = models.CharField(unique=True, max_length=10, null=True)
    email = models.CharField(unique=True, max_length=50)
    gender = models.CharField(
        choices=(('M', 'Mujer'), ('H', 'Hombre')), max_length=16, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    objects = UserManager()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'

    def get_short_name(self):
        return self.name
