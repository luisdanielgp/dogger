from django.urls import path, re_path
from .views import ListHour, DetailHour

app_name="hours"

urlpatterns = [
  path('hours/', ListHour.as_view(), name="listHour"),
  re_path(r'^hours/(?P<id>[0-9a-f-]+)/$', DetailHour.as_view(), name="detailHour")
]
