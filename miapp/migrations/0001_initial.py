# Generated by Django 4.2 on 2023-04-24 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernameee', models.CharField(default='', max_length=50)),
                ('phoneee', models.CharField(max_length=50)),
                ('adresss', models.CharField(max_length=50)),
                ('product_nameee', models.CharField(max_length=50)),
                ('sizeee', models.CharField(max_length=50)),
            ],
        ),
    ]
