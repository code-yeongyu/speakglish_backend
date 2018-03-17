from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model) :
    created = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey('auth.User', related_name='app', on_delete=models.CASCADE)
    doneAt = models.DateTimeField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    timer = models.IntegerField()
    timerLeft = models.IntegerField()

    class Meta :
        ordering = ('created', )