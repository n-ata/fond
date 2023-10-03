from django.db import models
from django.utils import timezone
import os
import uuid
from ckeditor.fields import RichTextField

def get_file_path(instance, filename):

    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('photos', filename)
    # return os.path.join('photos/'+instance.floor.apartment.name, filename)


class Menu(models.Model):
    name = models.CharField(max_length=1000)
    href = models.CharField(max_length=300)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Home(models.Model):
    banner = models.ImageField(upload_to=get_file_path, height_field=None, width_field=None, max_length=None, blank=True)
    title = models.CharField(max_length=1000)
    text = RichTextField(max_length=4000)

    def __str__(self):
        return self.title

class About(models.Model):
    banner = models.ImageField(upload_to=get_file_path, height_field=None, width_field=None, max_length=None, blank=True)
    title = models.CharField(max_length=1000)
    text = RichTextField(max_length=4000)

    def __str__(self):
        return self.title

class Helping(models.Model):
    icon = models.FileField(upload_to=get_file_path, blank=True)
    title = models.CharField(max_length=1000)
    text = RichTextField(max_length=4000)

    def __str__(self):
        return self.title

class Fond(models.Model):
    banner = models.ImageField(upload_to=get_file_path, height_field=None, width_field=None, max_length=None,
                               blank=True)
    title = models.CharField(max_length=200)
    text = RichTextField(max_length=4000)
    goal = models.IntegerField()
    raised = models.IntegerField()
    initialRasised = models.IntegerField(default=0)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Fond, self).save(*args, **kwargs)

class Blogs(models.Model):
    banner = models.ImageField(upload_to=get_file_path, height_field=None, width_field=None, max_length=None,
                               blank=True)
    title = models.CharField(max_length=200)
    text = RichTextField(max_length=4000)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Blogs, self).save(*args, **kwargs)

class Others(models.Model):
    makeadonation = models.CharField(max_length=100)
    aboutus = models.CharField(max_length=100)
    discoverme = models.CharField(max_length=100)
    helpingtoday = models.CharField(max_length=100)
    howwehelppeople = models.CharField(max_length=100)
    programs = models.CharField(max_length=100)
    ourdonationprograms = models.CharField(max_length=100)
    news = models.CharField(max_length=100)
    goal = models.CharField(max_length=100)
    raised = models.CharField(max_length=100)
    latestblog = models.CharField(max_length=100)
    readmore = models.CharField(max_length=100)
    footertext = models.CharField(max_length=100)
    navigation = models.CharField(max_length=100)
    contactus = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    support = models.CharField(max_length=100)
    supporttext = models.CharField(max_length=100)
    donate = models.CharField(max_length=100)
    copyright = models.CharField(max_length=100)

class BlogDetailsOther(models.Model):
    blogdetails = models.CharField(max_length=100)
    newsletter = models.CharField(max_length=100)
    enteremail = models.CharField(max_length=100)
    subscribe = models.CharField(max_length=100)
    recentposts = models.CharField(max_length=100)

class Payments(models.Model):
    fond = models.ForeignKey(Fond, on_delete=models.CASCADE)
    conversationId = models.CharField(max_length=200, default=0)
    value = models.FloatField()
    status = models.BooleanField(default=False, blank=True)
    message = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.conversationId

class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email