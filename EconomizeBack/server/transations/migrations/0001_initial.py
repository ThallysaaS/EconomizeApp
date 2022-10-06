# Generated by Django 3.2.8 on 2021-11-12 23:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Contas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('saldo', models.FloatField()),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=45)),
                ('valor', models.FloatField()),
                ('data', models.DateField()),
                ('tipo', models.CharField(max_length=255)),
                ('idConta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transations.contas')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('idCategorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transations.categorias')),
            ],
        ),
        migrations.AddField(
            model_name='categorias',
            name='idTransacoes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transations.transations'),
        ),
        migrations.AddField(
            model_name='categorias',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
