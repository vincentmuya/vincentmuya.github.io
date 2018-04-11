from django import forms
from tinymce.models import HTMLField

class FeedbackForm(forms.Form):
    email = forms.EmailField(label='Email',)
    question_Feedback = forms.CharField(
    widget=forms.Textarea(),
    )
