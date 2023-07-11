from django.shortcuts import render


def blog(request):
    ctx = {

    }
    return render(request, 'blog/blog.html', ctx)
