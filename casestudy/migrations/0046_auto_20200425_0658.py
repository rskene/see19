# Generated by Django 3.0.4 on 2020-04-25 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0045_travel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='visitors',
            field=models.FloatField(verbose_name='Visitors'),
        ),
    ]