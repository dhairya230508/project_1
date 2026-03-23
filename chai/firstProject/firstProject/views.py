from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello, world. this is home page")
    return render(request, 'otherpages/index.html')

def about(request):
    # return HttpResponse("hello, world. this is about page")
    return render(request, 'otherpages/about.html')

def contact(request):
    # return HttpResponse("this is Contact page")
    return render(request, 'otherpages/contact-us.html')