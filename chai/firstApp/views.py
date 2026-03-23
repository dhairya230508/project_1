from django.shortcuts import render
from .models import Contact
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def food(request):
    return render(request,'food.html')
def contact(request):
    return render(request,'contact.html')

def combo(request):
    return render(request,'combo.html')

from django.shortcuts import render, redirect
from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect('contact')  # reload page after submit

    return render(request, 'contact.html')