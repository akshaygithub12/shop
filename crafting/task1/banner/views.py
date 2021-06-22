from django.shortcuts import render
from .models import Menu1
# Create your views here.


def index(request):
    menu1 = Menu1.objects.all()
    return render(request,"index.html",{'Menu1':menu1})

