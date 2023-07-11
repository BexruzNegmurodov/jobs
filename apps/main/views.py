from django.shortcuts import render


def main(request):
    ctx = {

    }
    return render(request, 'main/index.html', ctx)
