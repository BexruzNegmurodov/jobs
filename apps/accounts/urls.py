from django.urls import path
from .views import candidate, login, register

app_name = 'candidate'

urlpatterns = [
    path('', candidate, name='candidate'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]
