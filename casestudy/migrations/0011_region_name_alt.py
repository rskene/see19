# Generated by Django 3.0.4 on 2020-04-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0010_region_country_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='name_alt',
            field=models.CharField(max_length=100, null=True, verbose_name='Alternative Name'),
        ),
    ]