# Generated by Django 4.2.4 on 2024-11-04 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=300)),
                ('nom', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('ville', models.CharField(max_length=200)),
                ('pays', models.CharField(max_length=300)),
                ('date_commande', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_commande'],
            },
        ),
    ]
