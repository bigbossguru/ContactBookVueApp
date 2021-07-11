from django.contrib import admin
from .models import ContactBook

# Register your models here.
class ContactBookAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'department')

admin.site.register(ContactBook, ContactBookAdmin)