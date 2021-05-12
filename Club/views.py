from django.shortcuts import render
from .models import Resource, User

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def resources(request):
     return render(request, 'Club/resources.html', {'resource_list': Resource.objects.all()})