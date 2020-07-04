from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    au = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    cr_date = models.DateTimeField(default=timezone.now)
