from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Blog)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)