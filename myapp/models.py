from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
    
    
    
    
    