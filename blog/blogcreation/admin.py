from django.contrib import admin#default login page
from . models import BlogPost

# Register your models here.
admin.site.register(BlogPost)#blogpost is the model