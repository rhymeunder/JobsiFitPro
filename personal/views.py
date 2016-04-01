from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")

@login_required
def index(request) :
    return render(request, 'personal/home.html')
@login_required
def contact(request) :
    return render(request, 'personal/basic.html', {'content':['If you would like to contact our company please email us at', 'jobsifit@gmail.com']})
                                                              