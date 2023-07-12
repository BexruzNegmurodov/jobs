from django.db import models
from ckeditor.fields import RichTextField


class Basic(models.Model):
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(Basic):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tags(Basic):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Blog(Basic):
    title = models.CharField(max_length=221)
    slug = models.SlugField(unique=True, null=True)
    image = models.ImageField(upload_to='blog/')
    description1 = RichTextField()
    the_main_part = RichTextField(null=True, blank=True)
    description2 = RichTextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tags, )
    author_name = models.CharField(max_length=221)
    author_image = models.ImageField(upload_to='authors/')
    the_author_is_words = models.TextField()


class Comment(Basic):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=221)
    email = models.EmailField()
    image = models.ImageField(upload_to='blog/comment/')
    message = models.TextField()
