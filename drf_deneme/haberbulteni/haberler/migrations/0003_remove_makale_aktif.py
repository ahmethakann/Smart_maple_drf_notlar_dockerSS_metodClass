# Generated by Django 4.1.5 on 2023-01-18 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haberler', '0002_alter_makale_yayimlanma_tarihi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='makale',
            name='aktif',
        ),
    ]
