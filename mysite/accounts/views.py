

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            msg='You have succesfully Registered'

            return redirect(request, "home.html",{'msg':msg})


    else:
        form = UserCreationForm()
        return render(request, "register.html", {'form': form})

