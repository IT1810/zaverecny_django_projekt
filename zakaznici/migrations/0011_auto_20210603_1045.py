# Generated by Django 3.2 on 2021-06-03 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zakaznici', '0010_auto_20210509_2250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tarif',
            options={},
        ),
        migrations.AlterOrderWithRespectTo(
            name='tarif',
            order_with_respect_to='operator',
        ),
    ]
