from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, null = True)
    title = models.CharField(max_length = 40)
    image = models.ImageField(upload_to = 'post/')
    description = HTMLField()
    github_link = models.CharField(max_length = 40)
    deployed_link = models.CharField(max_length = 40)

    def __str__(self):
        return self.title

    def save_project(self):
            self.save

# method to call objects from the database
    @classmethod
    def this_project(cls):
        pro = cls.objects.all()
        return pro

class FeedbackRecipients(models.Model):
    email = models.EmailField()
    question_Feedback = models.CharField(max_length=1000)
