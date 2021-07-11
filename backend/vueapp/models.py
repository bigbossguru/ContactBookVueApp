from django.db import models

# Create your models here.
class ContactBook(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    department = models.TextField()
