from django.contrib import admin
from .models import Application, Category, Status

# Register your models here.
admin.site.register(Application)
admin.site.register(Category)
admin.site.register(Status)