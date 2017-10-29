from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm


# Create your views here.d

# testing views

# method based view
@login_required
def home(request):
    return render(request,'home.html')
    #  return HttpResponse('hello welcome home')


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


def loginform(request):
    return render(request,'login.html')

@login_required
def profile(request):
    return HttpResponse("this is your profile")

def main(request):
    return render(request, 'index.html')
