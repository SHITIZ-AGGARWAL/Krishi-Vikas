# Generated by Django 3.1.3 on 2020-11-24 08:01

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default='Mew Delhi', max_length=255),
        ),
        migrations.AddField(
            model_name='customer',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63, null=True),
        ),
    ]
