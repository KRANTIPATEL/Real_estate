# Generated by Django 5.0.6 on 2024-06-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home_Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=25)),
                ('img_link', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=20)),
                ('Price', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=50)),
                ('beds', models.CharField(max_length=15)),
                ('bathroom', models.CharField(max_length=15)),
            ],
        ),
    ]
