from django.contrib import admin
from .models import Application, Category

# Register your models here.
# admin.site.register(Application)
admin.site.register(Category)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'status', 'created_at')
    list_filter = ('status', 'created_at')
