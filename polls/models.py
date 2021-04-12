from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=255)
    text=models.TextField()

    def __str__(self):
        return self.name

