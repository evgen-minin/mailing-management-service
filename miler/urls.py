from django.urls import path
from .views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, home_view, client_list_view

urlpatterns = [
    path('', home_view, name='home'),
    path('clients/', client_list_view, name='client_list'),
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
]
