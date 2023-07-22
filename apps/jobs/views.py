from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q


from .models import Job, Company, Category, Apply


def jobs(request):
    object_list = Job.objects.order_by('-id')
    search_category = request.GET.get('category')
    search_company = request.GET.get('company')
    location = request.GET.get('location')
    if search_company or search_category or location:
        print(search_company, search_category, location)
        object_list = object_list.filter(
            Q(category__name__exact=search_category) | Q(company__name__exact=search_company) | Q(
                location__contains=location))
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


def job_detail(request, **kwargs):
    obj = Job.objects.get(slug=kwargs.get('slug'))

    ctx = {
        'obj': obj
    }
    return render(request, 'jobs/job_details.html', ctx)
