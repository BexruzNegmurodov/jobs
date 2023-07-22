from django.contrib import admin
from .models import Category, Company, Job, Apply


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date')
    date_hierarchy = 'created_date'
    search_fields = ('name',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date')
    date_hierarchy = 'created_date'
    search_fields = ('name',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'category', 'time', 'created_date')
    date_hierarchy = 'created_date'
    search_fields = ('company', 'category', 'time')


@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'job')
    date_hierarchy = 'created_date'
    search_fields = ('name',)
