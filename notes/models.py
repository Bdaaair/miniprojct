from django.db import models

# Create your models here.
class Note(models.Model):
    Date = models.DateField()
    title = models.CharField(max_length=100)
    body = models.TextField()