# Generated by Django 4.1.5 on 2023-01-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haberler', '0004_makale_aktif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makale',
            name='aktif',
            field=models.BooleanField(default=True),
        ),
    ]
