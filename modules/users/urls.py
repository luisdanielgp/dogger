from django.urls import path, re_path
from .views import ListUser, DetailUser

app_name="users"

urlpatterns = [
  path('users/', ListUser.as_view(), name="listUser"),
  re_path(r'^users/(?P<id>[0-9a-f-]+)/$', DetailUser.as_view(), name="detailUser")
]
