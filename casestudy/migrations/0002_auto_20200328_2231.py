# Generated by Django 3.0.4 on 2020-03-28 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcases',
            name='region',
            field=models.CharField(max_length=100, verbose_name='Region'),
        ),
    ]