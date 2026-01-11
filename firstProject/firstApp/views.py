from django.shortcuts import render

# Create your views here.

def appHome(request):
    return render(request,'firstApp/app.html')
