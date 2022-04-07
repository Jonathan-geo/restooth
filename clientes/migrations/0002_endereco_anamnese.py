# Generated by Django 4.0 on 2022-04-07 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_cliente', models.CharField(max_length=255, unique=True)),
                ('rua', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=255)),
                ('complemento', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Anamnese',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_cliente', models.CharField(max_length=255, unique=True)),
                ('estaTratamentoMedico', models.BooleanField(default=False)),
                ('tomaMedicamento', models.BooleanField(default=False)),
                ('temAlergia', models.BooleanField(default=False)),
                ('esteveInternado', models.BooleanField(default=False)),
                ('jaDesmaiou', models.BooleanField(default=False)),
                ('temPressaoAlta', models.BooleanField(default=False)),
                ('doencaCardiaca', models.BooleanField(default=False)),
                ('doencaRespiratoria', models.BooleanField(default=False)),
                ('figado', models.BooleanField(default=False)),
                ('rins', models.BooleanField(default=False)),
                ('diabetes', models.BooleanField(default=False)),
                ('hepatite', models.BooleanField(default=False)),
                ('doencaGrave', models.BooleanField(default=False)),
                ('temSangramentoGengiva', models.BooleanField(default=False)),
                ('temSensibilidade', models.BooleanField(default=False)),
                ('temDorDente', models.BooleanField(default=False)),
                ('observacoesAnamnese', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
    ]