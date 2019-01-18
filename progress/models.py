from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Progress(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    details = models.TextField()
    added = models.DateField(default=datetime.now)
