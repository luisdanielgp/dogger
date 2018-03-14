from django.urls import path, re_path
from .views import ListOwner, DetailOwner

app_name="owners"

urlpatterns = [
  path('owners/', ListOwner.as_view(), name="listOwner"),
  re_path(r'^owners/(?P<id>[0-9a-f-]+)/$', DetailOwner.as_view(), name="detailOwner")
]
