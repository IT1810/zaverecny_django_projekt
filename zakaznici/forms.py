from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import *


class ZakaznikModelForm(ModelForm):
    class Meta:
        model = Zakaznik
        fields = ['jmeno', 'prijmeni', 'psc', 'ulice', 'mesto', 'cp', 'email', 'druhotne_sluzby']
        labels = {'jmeno': 'Jméno zákazníka','prijmeni': 'Přijmení zákazníka', 'psc':'PSČ','ulice':'Ulice', 'mesto':'Město', 'cp':'Číslo popisné', 'email':'Email', 'druhotne_sluzby':'Druhotné služby'}