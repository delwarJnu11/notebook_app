from django.db import models
from django.contrib.auth.models import User
from notes.constants import STATUS

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 500)
    tags = models.ManyToManyField(Tag)
    status = models.IntegerField(choices = STATUS, default= 1)
    created_on = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, related_name='users', on_delete = models.CASCADE)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title
    
