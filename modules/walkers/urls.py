from django.urls import path, re_path
from .views import ListWalker, DetailWalker

app_name="walkers"

urlpatterns = [
  path('walkers/', ListWalker.as_view(), name="listWalker"),
  re_path(r'^walkers/(?P<id>[0-9a-f-]+)/$', DetailWalker.as_view(), name="detailWalker")
]
