from unicodedata import name
from django.db import models

# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year_released = models.DateField()