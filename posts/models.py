from django.db import models


class Post(models.Model):  # This is a class that inherits from the models.Model class
    text = models.TextField()

    def __str__(self):
        return self.text[:50]  # This is a method that returns a string representation of the object

# Create your models here.
