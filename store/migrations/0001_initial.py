# Generated by Django 4.0.4 on 2022-06-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('PENDING', 'Pending'), ('FAILED', 'Failed'), ('COMPLETE', 'Complete')], default='PENDING', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]