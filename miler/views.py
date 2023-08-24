from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Client, Mailing, BlogArticle
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Count

def client_list_view(request):
    clients = Client.objects.all()

    context = {
        'clients': clients,
    }
    return render(request, 'miler/client_list.html', context)

def home_view(request):
    total_mailings = Mailing.objects.count()
    active_mailings = Mailing.objects.filter(status='started').count()

    latest_clients = Client.objects.all().order_by('-id')[:3]  
    clients = Client.objects.all()

    clients_with_mailings = [] 
    for client in clients:

        mailing_count = Mailing.objects.filter(client=client).count()

       
        clients_with_mailings.append({
            'client': client,
            'mailing_count': mailing_count,
        })

    random_articles = BlogArticle.objects.order_by('?')[:3]

    context = {
        'total_mailings': total_mailings,
        'active_mailings': active_mailings,
        'latest_clients': latest_clients,
        'clients_with_mailings': clients_with_mailings,
        'random_articles': random_articles,
    }
    return render(request, 'miler/home.html', context)

class MailingListView(ListView):
    model = Mailing
    template_name = 'mailer/mailing_list.html'
    context_object_name = 'mailings'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = Client.objects.annotate(num_mailings=Count('mailings'))
        
        context['clients'] = clients
        return context

    
class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailer/mailing_detail.html'
    context_object_name = 'mailing'

class MailingCreateView(CreateView):
    model = Mailing
    fields = '__all__'
    template_name = 'mailer/mailing_create.html'
    success_url = reverse_lazy('mailing_list')

class MailingUpdateView(UpdateView):
    model = Mailing
    fields = '__all__'
    template_name = 'mailer/mailing_update.html'
    success_url = reverse_lazy('mailing_list')

class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = '/mailings/'
    template_name = 'mailer/mailing_delete.html'

