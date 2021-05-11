from django.shortcuts import render
from django.views.generic import ListView
from zakaznici.models import *


# Create your views here.


def index(requests):

    num_customers = Zakaznik.objects.all().count()
    customers = Zakaznik.objects.order_by('prijmeni')[:5]
    contracts = Smlouva.objects.order_by('-zakaznik')
    context = {
        'num_customers': num_customers,
        'customers': customers,
        'contracts': contracts,
    }
    return render(requests, 'index.html', context=context)


class ZakaznikListView(ListView):
    model = Zakaznik
    context_object_name = 'prehled_zakazniku'
    extra_context = {'contracts': Smlouva.objects.all(),
                     'num_customers': Zakaznik.objects.all().count()}
    template_name = 'zakaznik/prehled.html'
