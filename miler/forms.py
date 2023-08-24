from django import forms
from .models import Newsletter, Message

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['send_time', 'frequency', 'status']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body']
