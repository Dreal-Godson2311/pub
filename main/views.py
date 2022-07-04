from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render (request, 'main/index.html',{})

def benefits(request):
    return render (request, 'main/benefits.html')

def contacts(request):
    return render (request, 'main/contacts.html')

def meetme(request):
    return render (request, 'main/meetme.html')

def services(request):
    return render (request, 'main/services.html')

def contactme(request):
    return render (request, 'main/contactme.html')

def contactmee(request):
    return render (request, 'main/contactme.html')
