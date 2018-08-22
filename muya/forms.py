from django import forms
from tinymce.models import HTMLField
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = []
