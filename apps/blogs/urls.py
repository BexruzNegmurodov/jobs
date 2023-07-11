from django.urls import path
from .views import blog

app_name = 'blogs'

urlpatterns = [
    path('', blog, name='blog')
]
