from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    phone = forms.CharField(max_length=15, label='Phone')
    email = forms.EmailField(validators=[EmailValidator()], label='Email')
    subject = forms.CharField(max_length=100, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')
