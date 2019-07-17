from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
            form = RegistrationForm()
    return render(request, "register.html", {'form': form})

def profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)

def profile_view(request, *args, **kwargs):
    return render(request,"profile.html")