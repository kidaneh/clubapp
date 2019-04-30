from django.shortcuts import render
from .models import Meeting, Minute, Resource, event

# Create your views here.
def index (request):
    return render (request, 'pythonapp/index.html')

def getResource(request):
    resource_list=Resource.objects.all()
    return render(request, 'pythonapp/Resource.html',{'resource_list':resource_list})
    

