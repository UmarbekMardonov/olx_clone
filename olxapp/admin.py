from django.contrib import admin
from .models import Category, Adds


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'objects')
