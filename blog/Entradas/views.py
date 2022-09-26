from django.shortcuts import render

from blog.Entradas.models import entrada

# Create your views here.

def index(request):
    entradas = entrada.objects.all()
    return render(request,'index.html',{'entradas':entradas})
