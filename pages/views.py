from django.shortcuts import render

def home(request):
    return render(request ,'pages/home.html')

def about(request):
    return render(request ,'pages/about.html')

def services(request):
    return render(request ,'pages/services.html')

def contact(request):
    return render(request ,'pages/contact.html')

def login(request):
    return render(request ,'pages/login.html')

def signup(request):
    return render (request ,'pages/signup.html')