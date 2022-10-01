from django.views.generic import ListView
from .models import Post


class HomePageView(ListView): # This is a class that inherits from the ListView class
    model = Post
    template_name = "home.html"
