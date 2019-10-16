# Generated by Django 2.2.4 on 2019-10-15 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familia_producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familia', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=128)),
                ('familia_producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.Familia_producto')),
            ],
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.Cliente')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='precios',
            field=models.ManyToManyField(through='administracion.Precio', to='administracion.Producto'),
        ),
    ]
