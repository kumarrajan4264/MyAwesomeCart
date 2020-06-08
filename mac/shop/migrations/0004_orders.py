# Generated by Django 3.0.5 on 2020-05-28 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=11)),
                ('city', models.CharField(max_length=110)),
                ('state', models.CharField(max_length=11)),
                ('zip_code', models.CharField(max_length=111)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
    ]
