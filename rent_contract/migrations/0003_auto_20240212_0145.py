# Generated by Django 3.2.7 on 2024-02-11 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent_contract', '0002_auto_20240204_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentcontract',
            name='contract_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='rentcontract',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rentcontract',
            name='start_rent_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='PayingDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_counter', models.SmallIntegerField()),
                ('date', models.DateField()),
                ('is_paid', models.BooleanField(default=False)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_contract.rentcontract')),
            ],
        ),
    ]
