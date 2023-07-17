from django.shortcuts import render, redirect
from .forms import CommentForm


def contact(request):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(".")
    ctx = {
        'form': form
    }
    return render(request, 'contact/contact.html', ctx)
