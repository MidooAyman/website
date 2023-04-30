from django.shortcuts import render
from .models import Login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def index(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    phone = request.POST.get('phone')
    adress = request.POST.get('adress')
    product_name = request.POST.get('product_name')
    size = request.POST.get('size')
    if username is not None:
        data = Login(username=username, adress=adress, phone=phone, product_name=product_name, size=size)
        data.save()
    return render(request, 'form.html')
  else:
         return render(request, 'form.html')




