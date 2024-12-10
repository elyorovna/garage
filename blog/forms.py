from django import forms

from blog.models import Email, Contact


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'text']
