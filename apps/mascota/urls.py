

from apps.mascota.views import index
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    url(r'^$', index),
]