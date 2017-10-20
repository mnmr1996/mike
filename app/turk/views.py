from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm


# Create your views here.d

# testing views

# method based view
def home(request):
    return HttpResponse('hello welcome home')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #return HttpResponseRedirect('http://localhost:8000/turk/login/')
            return redirect(home)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
    # some responds


def loginform(resquest):
    return HttpResponse("This will be the login page")
