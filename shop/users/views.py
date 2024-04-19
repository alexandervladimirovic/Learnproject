from django.shortcuts import render
from . import forms

def register(request):
    form = forms.NewUserForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)
