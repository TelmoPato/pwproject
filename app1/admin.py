from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from .models import Pessoa




admin.site.register(Pessoa)
