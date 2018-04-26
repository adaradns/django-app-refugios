
from apps.adopcion.views import index_adopcion
from django.urls import path
from django.conf.urls import url


urlpatterns = [
	url(r'^index$', index_adopcion)
]