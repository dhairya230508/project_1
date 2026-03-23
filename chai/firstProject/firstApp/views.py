from django.shortcuts import render
from .models import ChaiType
from django.shortcuts import get_object_or_404

# Create your views here.
def appHome(request):
    # here we get all chais from "DB"
    chais = ChaiType.objects.all()              #object   variable
    return render(request,'firstApp/app.html' , {'chais' : chais})


def chaiDetail(request, chai_id):
    chai = get_object_or_404(ChaiType, pk=chai_id)
    return render(request, 'firstApp/chaiDetail.html', {'chai':chai})

