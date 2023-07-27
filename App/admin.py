from django.contrib import admin
from .models import *


@admin.register(Receipe)
class Receipe_admin(admin.ModelAdmin):
    list_display = ['receipe_name', 'receipe_description', 'receipe_image']
