from django.shortcuts import render
from apps.jobs.models import Category


def main(request):
    object_list = Category.objects.order_by('-id')[:3]
    ctx = {
        'object_list': object_list
    }
    return render(request, 'main/index.html', ctx)
