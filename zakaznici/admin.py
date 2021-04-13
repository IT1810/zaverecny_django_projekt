from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Zakaznik)
admin.site.register(TelefonniCislo)
admin.site.register(Smlouva)
admin.site.register(Tarif)
admin.site.register(DruhotneSluzby)
admin.site.register(MobilniOperator)