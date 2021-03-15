from django.db import models
from ckeditor.fields import RichTextField


class Host(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


STATUS_CHOICES = (
    (0, 'draft'),
    (1, 'publish')
)


class Episode(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    podcast = models.CharField(max_length=200, default="https://share.transistor.fm/e/1493e91f/dark")
    excerpt = RichTextField(default="excerpt")
    content = RichTextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
