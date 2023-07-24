from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from .forms import AccountRegisterForm
from .models import Account

from apps.jobs.models import Apply

def candidate(request):
    object_list = Account.objects.filter(role=1)
    ctx = {
        'object_list': object_list
    }
    return render(request, 'account/candidate/candidate.html', ctx)


def candidate_detail(request, slug):
    worker = Account.objects.get(slug=slug)
    ctx = {
        'worker': worker
    }
    return render(request, 'account/candidate/candidate_detail.html', ctx)


def selected(request):
    jobs = Apply.objects.filter(candidate__email=request.user.email)
    print(type(jobs))
    ctx = {
        'jobs': jobs
    }
    return render(request, 'account/candidate/selected.html', ctx)


def mylogin(request):
    form = AuthenticationForm(request)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'User successfully authentication')
            return redirect('main:main')
    ctx = {
        'form': form
    }
    return render(request, 'account/login.html', ctx)


def register(request):
    form = AccountRegisterForm()
    if request.method == "POST":
        form = AccountRegisterForm(data=request.POST)
        if form.is_valid():
            messages.success(request, 'Account successfully created!')
            obj = form.save(commit=False)
            if not request.POST.get('role'):
                raise ValidationError('you should select a role')
            obj.role = int(request.POST.get('role'))
            obj.save()
            return redirect('accounts:login')
    ctx = {
        'form': form
    }
    return render(request, 'account/sin-up.html', ctx)


def mylogout(request):
    if request.method == "POST":
        logout(request)
        messages.error(request, 'logout')
        return redirect('main:main')
    return render(request, 'account/logout.html')


def profile(request):
    ctx = {

    }
    return render(request, 'account/profile.html', ctx)