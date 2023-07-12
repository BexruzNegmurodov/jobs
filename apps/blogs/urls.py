from django.urls import path
from .views import blog, blog_detail

app_name = 'blogs'

urlpatterns = [
    path('', blog, name='blog'),
    path('detail/<slug:slug>/', blog_detail, name='blog_detail'),
]
