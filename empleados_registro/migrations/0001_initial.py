# Generated by Django 3.2.2 on 2021-05-11 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrecompleto', models.CharField(max_length=100)),
                ('empleado_codigo', models.CharField(max_length=3)),
                ('movil', models.CharField(max_length=15)),
                ('posicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados_registro.posicion')),
            ],
        ),
    ]
