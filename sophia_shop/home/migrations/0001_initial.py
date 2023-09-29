# Generated by Django 4.2.5 on 2023-09-29 06:27

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
                ('prod_desc', models.CharField(max_length=200)),
                ('prod_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_added', models.DateTimeField(verbose_name='date added')),
            ],
        ),
    ]
