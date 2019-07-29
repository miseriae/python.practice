from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created, thanks for join {username}!')
            return redirect('main:main-homepage')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', context={'form': form})
