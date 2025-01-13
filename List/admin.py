from django.contrib import admin
from .models import Lists

@admin.register(Lists)

class ListAdmin(admin.ModelAdmin):
    list_display=('S_No','Items')
