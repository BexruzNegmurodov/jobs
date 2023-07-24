from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Job, Company, Category, Apply
from .forms import ApplyForm


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
    form = ApplyForm()
    if request.method == "POST":
        form = ApplyForm(data=request.POST, files=request.FILES or None)
        if form.is_valid():
            apply = form.save(commit=False)
            apply.candidate = request.user
            apply.job = obj
            apply.save()
            return redirect('.')
    ctx = {
        'obj': obj,
        'form': form,
    }
    return render(request, 'jobs/job_details.html', ctx)


def apply_job(request):
    object_list = Apply.objects.filter(job__author__email=request.user.email)
    ctx = {
        'object_list': object_list
    }
    return render(request, 'jobs/job_worker/apply_job.html', ctx)


def apply_detail(request, pk):
    worker = Apply.objects.get(id=pk)
    if request.method == "POST":
        result = request.POST.get('result')
        if result == '1':
            worker.to_accept = True
            worker.to_refuse = False
        else:
            worker.to_accept = False
            worker.to_refuse = True
        worker.save()
        return redirect("jobs:apply_job")
    ctx = {
        'worker': worker
    }
    return render(request, 'jobs/job_worker/apply_detail.html', ctx)
