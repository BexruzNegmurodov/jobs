from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify

from ckeditor.fields import RichTextField


class Basic(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(Basic):
    image = models.ImageField(upload_to='job/category', null=True)
    name = models.CharField(max_length=221)
    body = models.TextField(null=True)

    def __str__(self):
        return self.name


class Company(Basic):
    name = models.CharField(max_length=221)
    image = models.ImageField(upload_to='company/')

    def __str__(self):
        return self.name


class Job(Basic):
    TIME = (
        (1, 'full_time'),
        (2, 'part_time'),
        (3, 'three days a week'),
        (4, 'night time'),
        (5, "remote(time is not limited)")
    )
    GENDER = (
        (1, 'men'),
        (2, 'women'),
        (3, 'no difference')
    )
    slug = models.SlugField( null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=221)
    description = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    responsibility = RichTextField(null=True, blank=True)
    qualifications = RichTextField(null=True, blank=True)
    benefits = models.TextField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER)
    vacancy = models.IntegerField(default=1)
    time = models.IntegerField(choices=TIME)
    experience = models.CharField(max_length=221)
    salary = models.CharField(max_length=221)

    def __str__(self):
        return str(self.category)


class Apply(Basic):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=221)
    image = models.ImageField(upload_to='jobs/apply', null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()


def slug_post_save(instance, sender, created, *args, **kwargs):
    if created:
        instance.slug = slugify(f"{instance.company.name} {instance.category.name} {instance.id}", allow_unicode=True)
        instance.save()


post_save.connect(slug_post_save, sender=Job)
