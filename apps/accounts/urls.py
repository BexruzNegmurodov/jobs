from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .views import candidate, candidate_detail, mylogin, register, mylogout, profile

app_name = 'accounts'

urlpatterns = [
    path('', candidate, name='candidate'),
    path('candidate_detail/<slug:slug>/', candidate_detail, name='candidate_detail'),
    path('login/', mylogin, name='login'),
    path('register/', register, name='register'),
    path('logout/', mylogout, name='logout'),
    path('profile/', profile, name='profile'),

    path('password_change/', PasswordChangeView.as_view(template_name='account/change_pass/change_pass.html',
                                                        success_url=reverse_lazy("accounts:password_done")),
         name='password_change', ),
    path('password_done/', PasswordChangeDoneView.as_view(template_name='account/change_pass/change_done.html'),
         name='password_done', ),
]
