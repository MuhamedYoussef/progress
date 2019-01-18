from django.db import models


class Progress(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
