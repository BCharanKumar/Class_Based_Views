# Generated by Django 5.0.7 on 2024-11-20 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pname', models.CharField(max_length=50)),
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('product_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
    ]
