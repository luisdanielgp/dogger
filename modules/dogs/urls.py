from django.urls import path, re_path
from .views import ListGenericDog, DetailGenericDog

app_name="dogs"

urlpatterns = [
  path('dogs/', ListGenericDog.as_view(), name="listDog"),
  re_path(r'^dogs/(?P<pk>[0-9a-f-]+)/$', DetailGenericDog.as_view(), name="detailDog")
]
