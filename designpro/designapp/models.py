from django.db import models
from django.urls import reverse

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the application")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Status(models.Model):
    APP_STATUS = (
        ('n', 'New'),
        ('a', 'Accepted'),
        ('d', 'Done'),
    )

    status = models.CharField(max_length=1, choices=APP_STATUS, default='n', help_text="The status of the application")

    def __str__(self):
        return self.status