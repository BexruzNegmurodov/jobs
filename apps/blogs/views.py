from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Blog, Tags, Category
from .forms import CommentForm


def blog(request):
    objects = Blog.objects.order_by("-id")
    category = request.GET.get('category')
    tags = request.GET.get('tags')
    if category:
        objects = objects.filter(category__title__exact=category)
    if tags:
        objects = objects.filter(tags__title__exact=tags)
    paginator = Paginator(objects, 1)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    tags = Tags.objects.all()
    category = Category.objects.all()
    ctx = {
        'objects': page_obj,
        'tags': tags,
        'category': category,
    }
    return render(request, 'blog/blog.html', ctx)


def blog_detail(request, slug):
    obj = Blog.objects.get(slug=slug)
    tags = Tags.objects.all()
    category = Category.objects.all()
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
    ctx = {
        'obj': obj,
        'tags': tags,
        'category': category,
    }
    return render(request, 'blog/blog_details.html', ctx)
