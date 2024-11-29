from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the application")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('AdvUser', on_delete=models.SET_NULL, null=True)

    APP_STATUS = (
        ('n', 'New'),
        ('a', 'Accepted'),
        ('d', 'Done'),
    )

    status = models.CharField(max_length=1, choices=APP_STATUS, default='n', help_text="The status of the application")

    def get_absolute_url(self):
        return reverse('designapp-detail', args=[str(self.name)])

    def __str__(self):
        return '%s, %s (%s)' % (self.created_at, self.name, self.status)

    class Meta:
        ordering = ['-created_at']


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True,
                                       db_index=True, verbose_name='Have you been activated?')
    send_messages = models.BooleanField(default=True, verbose_name='Would you like to get new comments notification?')

    class Meta(AbstractUser.Meta):
        pass

