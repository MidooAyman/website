from django.db import models

# Create your models here.

class Destination(models.Model):
   
    name = models.CharField(max_length=100, verbose_name='Product Name')
    img= models.ImageField(upload_to='pics')
    ORIGINAL = 'OR'
    MIRROR = 'MI'
    EGYPTIAN = 'EG'
    SHIRTS = 'SH'
    JACKETS = 'JA'
    Other = 'OT'
    CHOICES = [
        (ORIGINAL, 'Original'),
        (MIRROR, 'Mirror'),
        (EGYPTIAN, 'Egyptian'),
        (SHIRTS, 'SHIRTS'),
        (JACKETS, 'JACKETS'), 
        (Other, 'Other'),
    ]
    des = models.CharField(max_length=2, choices=CHOICES)
    price= models.IntegerField()
    pricee = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    special= models.BooleanField(default=False)
    later= models.BooleanField(default=False)
    description = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
