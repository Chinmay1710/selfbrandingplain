"""Forms for portfolio_app."""

from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name',
                'id': 'id_name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your@email.com',
                'id': 'id_email',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject',
                'id': 'id_subject',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message here...',
                'rows': 5,
                'id': 'id_message',
            }),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }
