from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Count
from miler.forms import MailingForm, MessageForm
from django.urls import reverse
from miler.models import Client, Mailing 
from blog.models import BlogPost
import random


def client_list_view(request):
    clients = Client.objects.all()

    context = {
        'clients': clients,
    }
    return render(request, 'miler/client_list.html', context)

def home_view(request):
    total_mailings = Mailing.objects.count()
    active_mailings = Mailing.objects.filter(status='started').count()
    unique_clients = Client.objects.distinct().count()

    all_articles = BlogPost.objects.all()
    if len(all_articles) >=3:
        random_articles = random.sample(list(all_articles), 3)
    else:
         random_articles = all_articles
         
    return render(request, 'miler/home.html', {
        'total_mailings': total_mailings,
        'active_mailings': active_mailings,
        'unique_clients': unique_clients,
        'random_articles': random_articles,
    })
   

class MailingListView(ListView):
    model = Mailing
    template_name = 'miler/mailing_list.html'
    context_object_name = 'mailings'
    
    def get(self, request):
        mailings = Mailing.objects.all()
        clients = Client.objects.annotate(num_mailings=Count('mailings')) 
        return render(request, 'miler/mailing_list.html', {'mailings': mailings, 'clients': clients})

    
class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'miler/mailing_detail.html'
    context_object_name = 'mailing'

class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'miler/mailing_create.html'

    def form_valid(self, form):
        print("form_valid method called")
        self.object = form.save(commit=False)
        self.object.user = self.request.user  
        self.object.save()
        self.save_message()
        return super().form_valid(form)

    def save_message(self):
        print("save_message method called")
        message_form = MessageForm(self.request.POST)
        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.mailing = self.object
            message.save()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        context['message_form'] = MessageForm()
        return context

    def get_success_url(self):
        print("get_success_url method called")
        return reverse('mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'miler/mailing_update.html'
    success_url = reverse_lazy('mailing_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['message_form'] = MessageForm(self.request.POST, instance=self.object.message_set.first())
        else:
            context['message_form'] = MessageForm(instance=self.object.message_set.first())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        message_form = context['message_form']
        if message_form.is_valid():
            message_form.save()
        return super().form_valid(form)



class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = '/mailing_list/'
    template_name = 'miler/mailing_delete.html'
    context_object_name = 'object'
