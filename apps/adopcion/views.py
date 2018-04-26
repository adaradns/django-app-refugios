from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index_adopcion(request):
	return HttpResponse("Pagina principal Adopcion")

