from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
# Create your models here.


class MobilniOperator(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Jméno mobilního operátora')
    psc = models.PositiveIntegerField(validators=[MinValueValidator(10000), MaxValueValidator(99999)],
                                      verbose_name='Poštovní směrovací číslo')
    ulice = models.CharField(max_length=20, verbose_name='Ulice')
    mesto = models.CharField(max_length=30, verbose_name='Město')
    cp = models.CharField(max_length=4, verbose_name='Číslo popisné')
    kontakt = models.PositiveIntegerField(validators=[MinValueValidator(100000000), MaxValueValidator(999999999)],
                                        default=111111111, verbose_name='Telefonni číslo')

    class Meta:
        ordering = ['nazev']

    def __str__(self):
        return f'Nazev: {self.nazev} kontakt: {self.kontakt}'


class DruhotneSluzby(models.Model):
    nazev = models.CharField(max_length=45, verbose_name='Nazev druhotné služby')
    cena = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Cena služeb za měsíc')
    popis = models.TextField(blank=True, null=True, verbose_name='Popis sluzby')
    operator = models.ForeignKey(MobilniOperator, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nazev']

    def __str__(self):
        return f'Druhotna sluzba operatora: {self.operator}, nazev: {self.nazev}, cena : {self.cena}'


class Zakaznik(models.Model):
    jmeno = models.CharField(max_length=30, verbose_name='Křestní jméno')
    prijmeni = models.CharField(max_length=30, verbose_name='Příjmení')
    psc = models.PositiveIntegerField(validators=[MinValueValidator(10000), MaxValueValidator(99999)],
                                      verbose_name='Poštovní směrovací číslo')
    ulice = models.CharField(max_length=20, verbose_name='Ulice', blank=True)
    mesto = models.CharField(max_length=30, verbose_name='Město')
    cp = models.CharField(max_length=4, verbose_name='Číslo popisné')
    email = models.EmailField(max_length=50, unique=True, blank=True,null=True, verbose_name='Email zákazníka')
    druhotne_sluzby = models.ManyToManyField(DruhotneSluzby, blank=True, null=True,
                                             help_text='Select a secondary service of mobile operator which you use')

    class Meta:
        ordering = ['prijmeni']

    def __str__(self):
        return f'Jmeno: {self.jmeno}, prijmeni: {self.prijmeni}, email: {self.email}'


class TelefonniCislo(models.Model):
    zakaznik = models.ForeignKey(Zakaznik, on_delete=models.CASCADE)
    predvolba = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999)], verbose_name='Předvolba', blank=True, null=True, default="420")
    cislo = models.PositiveIntegerField(validators=[MinValueValidator(100000000), MaxValueValidator(999999999)],
                                        default=111111111, verbose_name='Telefonni číslo')

    class Meta:
        ordering = ['cislo']

    def __str__(self):
        return f'Telefonní cislo: +{self.predvolba} {self.cislo},  {self.zakaznik}'


class Tarif(models.Model):
    nazev = models.CharField(max_length=40,verbose_name='Nazev tarifu')
    cena = models.DecimalField(max_digits=7,decimal_places=2, verbose_name='Cena tarifu')
    operator = models.ForeignKey(MobilniOperator, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['operator']

    def __str__(self):
        return f'Nazev: {self.nazev}, cena: {self.cena}, operator: {self.operator}'


class Smlouva(models.Model):
    datum_uzavreni = models.DateField(blank=True, null=True, verbose_name='Datum uzavření')
    zakaznik = models.ForeignKey(Zakaznik, on_delete=models.CASCADE)
    tarif = models.ForeignKey(Tarif, on_delete=models.CASCADE)
    operator = models.ForeignKey(MobilniOperator, on_delete=models.CASCADE)

    class Meta:
        ordering = ['datum_uzavreni']

    def __str__(self):
        return f'Zakaznik: {self.zakaznik.jmeno} {self.zakaznik.prijmeni}, operator: {self.operator.nazev}, tarif: {self.tarif.nazev}'


