from django.contrib import admin
from .models import Client, Mailing, Message, DeliveryAttempt

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name')

@admin.register(Mailing)  # Замени Newsletter на Mailing
class MailingAdmin(admin.ModelAdmin):  # Замени NewsletterAdmin на MailingAdmin
    list_display = ('__str__', 'status', 'send_time')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'mailing')  # Замени newsletter на mailing

@admin.register(DeliveryAttempt)
class DeliveryAttemptAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'message', 'timestamp', 'status')
