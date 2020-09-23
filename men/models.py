from django.db import models

# Create your models here.
class Display(models.Model):
    title = models.CharField(max_length=60)
#    date = models.DateField(auto_now=False, blank=True)
    url = models.URLField(blank=True)
    imag = models.ImageField(upload_to='men/images/')
    bdgd = models.ImageField(upload_to='men/images/',blank=True)
    desc = models.TextField(max_length=600)
    def __str__(self):
        return self.title + self.url + self.desc

class Display2(models.Model):
    title = models.CharField(max_length=60)
    desc = models.CharField(max_length=60)
    date = models.DateField(auto_now=False)
    url = models.URLField(blank=True)
    imag = models.ImageField(upload_to='men/images/')
    bdgd = models.ImageField(upload_to='men/images/',blank=True)
    def __str__(self):
        return self.title

class Display3(models.Model):
    title = models.CharField(max_length=60)
    desc = models.CharField(max_length=60)
    date = models.DateField(auto_now=False)
    url = models.URLField(blank=True)
    imag = models.ImageField(upload_to='men/images/')
    bdgd = models.ImageField(upload_to='men/images/',blank=True)
    def __str__(self):
        return self.title
