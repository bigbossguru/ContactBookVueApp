from django.db import models

# Create your models here.
class ContactBook(models.Model):
    firstname = models.CharField(verbose_name="Firstname", max_length=100)
    lastname = models.CharField(verbose_name="Lastname", max_length=100)
    mobile_phone = models.CharField(verbose_name="Mobile phone", max_length=100)
    email = models.EmailField(verbose_name="Email", max_length=100)
    department = models.CharField(verbose_name="Department", max_length=100)


