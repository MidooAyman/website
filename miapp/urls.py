from django.urls import path

from . import views

urlpatterns = [

    path('form.html', views.index , name='index'),
]