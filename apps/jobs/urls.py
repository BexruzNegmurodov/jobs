from django.urls import path
from .views import jobs

app_name = 'jobs'

urlpatterns = [
    path('', jobs, name='jobs')
]
