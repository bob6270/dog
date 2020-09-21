from django.shortcuts import render
from .models import Display
from .models import Display2
from .models import Display3
# Create your views here.
def home(request):
    arg = Display.objects.all()
    return render(request, 'men/home.html',{'args':arg})
def page2(request):
    arg = Display2.objects.all()

    return render(request, 'men/page2.html',{ 'arg':arg })
def page3(request):
    arg = Display3.objects.all()
    return render(request, 'men/page3.html',{ 'arg':arg })
