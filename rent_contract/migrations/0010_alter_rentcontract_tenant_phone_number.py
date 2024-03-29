# Generated by Django 3.2.7 on 2024-02-21 17:27

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('rent_contract', '0009_alter_rentcontract_start_rent_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentcontract',
            name='tenant_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
