from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Blog, Tags, Category, Comment
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
    comment = Comment.objects.filter(blog_id=obj.id, reply_to_comment__isnull=True)
    reply_to_comment_id = request.GET.get('reply')
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = obj
            comment.reply_to_comment_id = reply_to_comment_id
            comment.save()
        return redirect(".")
    ctx = {
        'obj': obj,
        'tags': tags,
        'form': form,
        'category': category,
        'comment': comment,
    }
    return render(request, 'blog/blog_details.html', ctx)
