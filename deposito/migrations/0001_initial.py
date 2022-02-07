# Generated by Django 4.0.2 on 2022-02-03 18:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id_dep', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantia', models.FloatField()),
                ('data_dep', models.DateField()),
                ('cliente_cpf_dep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
            ],
        ),
    ]
