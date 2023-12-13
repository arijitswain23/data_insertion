from django.shortcuts import render

# Create your views here.
from app.models import *

def display_state(request):
    QLSO=State.objects.all()
    d={'State':QLSO}
    return render(request,'display_state.html',context=d)


def display_capital(request):
    QLCO=Capital.objects.all()
    d={'Capital':QLCO}
    return render(request,'display_capital.html',d)