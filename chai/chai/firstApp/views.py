from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def food(request):
    return render(request,'food.html')
def combo(request):
    return render(request,'combo.html')