from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from apps.jobs.models import Category
from .utils import avatar_path, cv_path


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra):
        if not email:
            raise ValueError("User should have an email")
        user = self.model(email=email, **extra)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra):
        user = self.create_user(email=email, password=password, **extra)
        user.is_staff = True
        user.is_superuser = True
        user.role = 0
        user.save()
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    ROLE = (
        (0, 'Staff'),
        (1, 'Candidate'),
        (2, 'Recruiter'),
    )

    email = models.EmailField(max_length=221, unique=True)
    first_name = models.CharField(max_length=221, null=True)
    last_name = models.CharField(max_length=221, null=True)
    avatar = models.ImageField(null=True, blank=True, upload_to=avatar_path)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    role = models.IntegerField(choices=ROLE, null=True)
    cv = models.FileField(upload_to=cv_path, null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    EMAIL_FIELD = ''
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return self.email

    def full_name(self):
        name_list = []
        if self.first_name:
            name_list.append(self.first_name)
        if self.last_name:
            name_list.append(self.last_name)
        name_str = " ".join(name_list)
        if name_str:
            return name_str
        return self.email
