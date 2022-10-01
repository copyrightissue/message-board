from django.contrib import admin
from .models import Post

admin.site.register(Post)  # This is a class that inherits from the models.Model class

# Register your models here.
