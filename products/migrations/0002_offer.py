# Generated by Django 3.2.9 on 2021-11-17 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=512)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
