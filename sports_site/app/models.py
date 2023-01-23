from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
import re


class Article(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    article_date = models.DateField(auto_now_add=True)
    snippet = models.CharField(max_length=255)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article', args=(str(self.id)))        
        return reverse('home')

class Podcast(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # video = models.VideoField()

    def save(self, *args, **kwargs):
        match = re.search(r'(?<=v=)[^&#]+', self.url)
        self.url = match.group(0) 
        super(Podcast, self).save(*args, **kwargs)

    def __str__(self):
        return self.title