from django.db import models
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
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.CharField(max_length=221)
    speciality = models.CharField(max_length=221)
    image = models.ImageField(upload_to='jobs/')
    description = RichTextField()
    gender = models.IntegerField(choices=GENDER)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    responsibility = RichTextField(null=True, blank=True)
    qualifications = RichTextField(null=True, blank=True)
    Benefits = models.TextField(null=True, blank=True)
    vacancy = models.IntegerField(default=1)
    time = models.IntegerField(choices=TIME)
    experience = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.speciality


class Apply(Basic):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=221)
    image = models.ImageField(upload_to='jobs/apply', null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
