from django import forms
from miler.models import Mailing, Message

class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['send_time', 'frequency', 'status', 'client']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body']
