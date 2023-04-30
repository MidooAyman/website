from django.shortcuts import render
from .models import Destination

# Create your views here.

def home(request):
    
    dest = Destination.objects.all()
    
    return render(request, 'home.html', {'dest': dest})


def home(request):
    if request.method == 'GET':
        category = request.GET.get('category')
        if category == 'Mirror':
            destinations = Destination.objects.filter(des='MI')
        elif category == 'original':
            destinations = Destination.objects.filter(des='OR')
        elif category == 'Egyptian':
            destinations = Destination.objects.filter(des='EG')
        elif category == 'SHIRTS':
            destinations = Destination.objects.filter(des='SH')    
        elif category == 'JACKETS':
            destinations = Destination.objects.filter(des='JA')  
        elif category == 'Other':
            destinations = Destination.objects.filter(des='OT')            
        else:
            destinations = Destination.objects.all()
    else:
        destinations = Destination.objects.all()

    context = {'dest': destinations}
    return render(request, 'home.html', context)

def index(request):
    return render(request, 'index.html')