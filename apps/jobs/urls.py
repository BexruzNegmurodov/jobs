from django.urls import path
from .views import jobs, job_detail, apply_job, apply_detail

app_name = 'jobs'

urlpatterns = [
    path('', jobs, name='jobs'),
    path('job_detail/<slug:slug>/', job_detail, name='job_detail'),
    path('apply_job/', apply_job, name='apply_job'),
    path('apply_detail/<int:pk>/', apply_detail, name='apply_detail'),
]
