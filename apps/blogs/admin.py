from django.contrib import admin
from .models import Category, Tags, Blog, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modified_date', 'created_date')
    search_fields = ('title',)
    list_filter = ('modified_date', 'created_date')


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modified_date', 'created_date')
    search_fields = ('title',)
    list_filter = ('modified_date', 'created_date')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'title', 'created_date')
    readonly_fields = ('modified_date', 'created_date')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    search_fields = ('title', 'author_name')
    list_filter = ('modified_date', 'created_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'name', 'modified_date', 'created_date')
    search_fields = ('name', 'blog')
    list_filter = ('modified_date', 'created_date')
