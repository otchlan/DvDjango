from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            msg='You have succesfully Registered'

            return render(request, 'templates/home.html',{'msg':msg})
        else
            form = UserCreationForm()

        args = {'form': form}
        return render(request, 'templates/reg_form.html', args)