# Generated by Django 3.0.4 on 2020-04-10 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0031_auto_20200410_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='country_key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='casestudy.Country'),
        ),
        migrations.AlterField(
            model_name='country',
            name='alpha2',
            field=models.CharField(max_length=2, null=True, verbose_name='Alpha-2 Code'),
        ),
        migrations.AlterField(
            model_name='country',
            name='alpha3',
            field=models.CharField(max_length=3, null=True, verbose_name='Alpha-3 Code'),
        ),
        migrations.AlterField(
            model_name='country',
            name='numeric',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Numeric Code'),
        ),
    ]