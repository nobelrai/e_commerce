# Generated by Django 5.0.1 on 2024-01-25 12:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('pants', 'Pants'), ('shirts', 'Shirts'), ('shoes', 'Shoes'), ('jackets', 'Jackets')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(limit_value=0.01), django.core.validators.MaxValueValidator(limit_value=9999.99)])),
                ('description', models.TextField(max_length=100)),
                ('size', models.CharField(choices=[('xs', 'XS'), ('s', 'S'), ('l', 'L'), ('xl', 'XL'), ('xll', 'XLL')], max_length=20)),
                ('color', models.CharField(choices=[('red', 'Red'), ('green', 'Green'), ('blue', 'Blue'), ('black', 'Black'), ('yellow', 'Yellow'), ('pink', 'Pink'), ('brown', 'Brown')], max_length=20)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]