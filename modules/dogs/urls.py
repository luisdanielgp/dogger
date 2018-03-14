from django.urls import path, re_path
from .views import ListDog, DetailDog

app_name="dogs"

urlpatterns = [
  path('dogs/', ListDog.as_view(), name="listDog"),
  re_path(r'^dogs/(?P<id>[0-9a-f-]+)/$', DetailDog.as_view(), name="detailDog")
]
