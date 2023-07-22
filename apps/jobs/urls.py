from django.urls import path
from .views import jobs, job_detail

app_name = 'jobs'

urlpatterns = [
    path('', jobs, name='jobs'),
    path('job_detail/<slug:slug>/', job_detail, name='job_detail'),
]
