from django.urls import path, re_path
from .views import ListWalk, DetailWalk

app_name="walks"

urlpatterns = [
  path('walks/', ListWalk.as_view(), name="listWalk"),
  re_path(r'^walks/(?P<id>[0-9a-f-]+)/$', DetailWalk.as_view(), name="detailWalk")
]
