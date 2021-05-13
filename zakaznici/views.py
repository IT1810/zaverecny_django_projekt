from django.shortcuts import render
from django.views.generic import ListView, DetailView
from zakaznici.models import *


# Create your views here.


def index(requests):

    num_customers = Zakaznik.objects.all().count()
    num_tarify = Tarif.objects.all().count()
    num_sluzby = DruhotneSluzby.objects.all().count()
    customers = Zakaznik.objects.order_by('prijmeni')[:5]
    contracts = Smlouva.objects.order_by('-zakaznik')
    tarify = Tarif.objects.all()
    sluzby = DruhotneSluzby.objects.all()
    num_sluzby
    context = {
        'num_customers': num_customers,
        'num_tarify': num_tarify,
        'num_sluzby': num_sluzby,
        'customers': customers,
        'contracts': contracts,
        'sluzby': sluzby,
        'tarify': tarify,
    }
    return render(requests, 'index.html', context=context)


class ZakaznikListView(ListView):
    model = Zakaznik
    context_object_name = 'prehled_zakazniku'
    extra_context = {'contracts': Smlouva.objects.all(),
                     'num_customers': Zakaznik.objects.all().count()}
    template_name = 'zakaznik/prehled.html'

class ZakaznikDetailView(DetailView):
    model = Zakaznik
    context_object_name = 'podrobnosti_zakaznika'
    template_name = 'zakaznik/podrobnosti.html'
    extra_context = {'contracts': Smlouva.objects.all()}
