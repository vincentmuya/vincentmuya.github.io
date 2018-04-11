from django.contrib import admin
from .models import Project,FeedbackRecipients

# Register your models here.
admin.site.register(Project)
admin.site.register(FeedbackRecipients)
