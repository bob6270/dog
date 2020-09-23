from django.db import models

# Create your models here.
class Display(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateField(auto_now=False)
    url = models.URLField(blank=True)
    imag = models.ImageField(upload_to='men/images/')
    bdgd = models.ImageField(upload_to='men/images/',blank=True)
    desc = models.CharField(max_length=200)


class Display2(models.Model):
    title = models.CharField(max_length=60)
    desc = models.CharField(max_length=60)
    date = models.DateField(auto_now=False)
    url = models.URLField(blank=True)
    imag = models.ImageField(upload_to='men/images/')

class Display3(models.Model):
    title = models.CharField(max_length=60)
    desc = models.CharField(max_length=60)
    date = models.DateField(auto_now=False)
    url = models.URLField(blank=True)
    imag = models.ImageField(upload_to='men/images/')
