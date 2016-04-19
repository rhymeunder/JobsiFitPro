from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import RegisterFormEmployer




def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterFormEmployer(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/employerbase/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterFormEmployer()

    return render(request, 'name.html', {'form': form})

# employers pages
#@login_required(login_url="login/")

def employerbase(request):
	return render(request, "employerbase.html")

def employerdash(request):
	return render(request, "employerdash.html")

def employerfaq(request):
	return render(request, "employerfaq.html")

def employerservice(request):
	return render(request, "employerservice.html")

def employeraccount(request):
	return render(request, "employeraccount.html")

def employerabout(request):
	return render(request, "employerabout.html")

def search(request):
	return render(request, "search.html")




#jobseekers pages
def seekerbase(request):
    return render(request, "seekerbase.html")

def seekerdash(request):
    return render(request, "seekerdash.html")

def seekerfaq(request):
    return render(request, "seekerfaq.html")

def seekerreg(request):
	return render(request, "seekerreg.html")

def seekerservice(request):
    return render(request, "seekerservice.html")

def seekeraccount(request):
    return render(request, "seekeraccount.html")

def seekeredu(request):
    return render(request, "seekeredu.html")

def seekerupload(request):
    return render(request, "seekerupload.html")

def seekerabout(request):
    return render(request, "seekerabout.html")

class IndexView(TemplateView):
	template_name = 'employerbase.html'