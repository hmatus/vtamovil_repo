# Generated by Django 2.2.4 on 2019-10-15 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_auto_20191015_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='ciudad',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='razon_social',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rut',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='comuna',
            name='comuna',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='condicion_de_pago',
            name='condicion_de_pago',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='condicion_de_pago',
            name='dias',
            field=models.SmallIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='familia_producto',
            name='familia',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='producto',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
