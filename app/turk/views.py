from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


# Create your views here.d

# testing views

# method based view

def signup(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(HttpResponse("signed up"))
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    # some responds
def loginform(resquest, *args, **kwargs):
    return HttpResponse("This will be the login page")
