# Generated by Django 4.0 on 2022-04-07 22:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimentacoes',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_cliente', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=255)),
                ('data', models.DateField()),
                ('tipoMorango', models.CharField(max_length=255)),
                ('qtdMorango', models.FloatField()),
                ('precoCaixaMorango', models.FloatField()),
                ('vendaMorango', models.IntegerField(max_length=1)),
                ('observacoes', models.TextField(null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
    ]
