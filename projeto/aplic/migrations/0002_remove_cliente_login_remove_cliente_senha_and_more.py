# Generated by Django 4.2.5 on 2023-10-05 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='login',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='senha',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='login',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='senha',
        ),
    ]