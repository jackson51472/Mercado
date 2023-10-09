# Generated by Django 4.2.5 on 2023-10-05 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0009_endereco_endereco_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='endereco_cliente',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplic.cliente'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='endereco_fornecedor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplic.fornecedor'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='endereco_funcionario',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplic.funcionario'),
        ),
    ]