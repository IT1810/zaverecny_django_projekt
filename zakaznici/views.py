from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from zakaznici.models import *
from zakaznici.forms import ZakaznikModelForm


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

class TarifListView(ListView):
    model = MobilniOperator
    template_name = 'blocks/tarify.html'
    context_object_name = 'operatori'
    queryset = MobilniOperator.objects.order_by('nazev').all()

class ZakaznikCreateView(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    model = Zakaznik
    success_url = reverse_lazy('prehled_zakazniku')
    template_name = 'zakaznik/zakaznik_form.html'
    fields = ['jmeno', 'prijmeni', 'psc', 'ulice', 'mesto', 'cp', 'email', 'druhotne_sluzby']
    login_url = '/accounts/login/'
    permission_required = 'zakaznici.add_zakaznik'


class ZakaznikUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    model = Zakaznik
    success_url = reverse_lazy('prehled_zakazniku')
    template_name = 'zakaznik/zakaznik_bootstrap_form.html'
    form_class = ZakaznikModelForm
    login_url = '/accounts/login/'
    permission_required = 'zakaznici.change_zakaznik'



class ZakaznikDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Zakaznik
    success_url = reverse_lazy('prehled_zakazniku')
    login_url = '/accounts/login/'
    permission_required = 'zakaznici.delete_zakaznik'