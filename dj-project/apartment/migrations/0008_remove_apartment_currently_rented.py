# Generated by Django 3.2.7 on 2024-02-18 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0007_apartment_is_rented'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='currently_rented',
        ),
    ]