from django.shortcuts import render


def candidate(request):
    ctx = {

    }
    return render(request, 'account/candidate.html', ctx)


def login(request):
    ctx = {

    }
    return render(request, 'account/login.html', ctx)


def register(request):
    ctx = {

    }
    return render(request, 'account/sin-up.html', ctx)
