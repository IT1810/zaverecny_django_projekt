# Generated by Django 3.2 on 2021-04-13 20:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DruhotneSluzby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=45, verbose_name='Nazev druhotné služby')),
                ('cena', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cena služeb za měsíc')),
                ('popis', models.TextField(blank=True, null=True, verbose_name='Popis sluzby')),
            ],
            options={
                'ordering': ['nazev'],
            },
        ),
        migrations.CreateModel(
            name='MobilniOperator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=100, verbose_name='Jméno mobilního operátora')),
                ('psc', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(99999)], verbose_name='Poštovní směrovací číslo')),
                ('ulice', models.CharField(max_length=20, verbose_name='Ulice')),
                ('mesto', models.CharField(max_length=30, verbose_name='Město')),
                ('cp', models.CharField(max_length=4, verbose_name='Číslo popisné')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, unique=True, verbose_name='Email operátora')),
            ],
            options={
                'ordering': ['nazev'],
            },
        ),
        migrations.CreateModel(
            name='Zakaznik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=30, verbose_name='Křestní jméno')),
                ('prijmeni', models.CharField(max_length=30, verbose_name='Příjmení')),
                ('psc', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(99999)], verbose_name='Poštovní směrovací číslo')),
                ('ulice', models.CharField(max_length=20, verbose_name='Ulice')),
                ('mesto', models.CharField(max_length=30, verbose_name='Město')),
                ('cp', models.CharField(max_length=4, verbose_name='Číslo popisné')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, unique=True, verbose_name='Email zákazníka')),
                ('druhotne_sluzby', models.ManyToManyField(help_text='Select a secondary service of mobile operator which you use', to='zakaznici.DruhotneSluzby')),
            ],
            options={
                'ordering': ['prijmeni'],
            },
        ),
        migrations.CreateModel(
            name='TelefonniCislo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predvolba', models.PositiveIntegerField(blank=True, default='420', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)], verbose_name='Předvolba')),
                ('zakaznik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zakaznici.zakaznik')),
            ],
            options={
                'ordering': ['zakaznik'],
            },
        ),
        migrations.AddField(
            model_name='druhotnesluzby',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zakaznici.mobilnioperator'),
        ),
    ]
