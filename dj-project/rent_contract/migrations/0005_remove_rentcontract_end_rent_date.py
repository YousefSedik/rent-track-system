# Generated by Django 3.2.7 on 2024-02-12 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent_contract', '0004_payingdates_is_canceled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentcontract',
            name='end_rent_date',
        ),
    ]
