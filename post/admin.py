from django.contrib import admin

# Register your models here.
from post.models import BlogPost

admin.site.register(BlogPost)
