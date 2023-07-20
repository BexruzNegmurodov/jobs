from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Job, Company, Category, Apply


def jobs(request):
    object_list = Job.objects.order_by('-id')
    paginator = Paginator(object_list, 3)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    category = Category.objects.all()
    company = Company.objects.all()
    ctx = {
        'object_list': page_obj,
        'category': category,
        'company': company,
    }
    return render(request, 'jobs/borwse_job.html', ctx)
