from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Contact(models.Model):
    Name = models.CharField(max_length = 40)
    email = models.EmailField()
    Question_or_Feedback = HTMLField()

    def __str__(self):
        return self.name
