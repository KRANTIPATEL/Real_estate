# Generated by Django 5.0.6 on 2024-07-03 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeproperty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_property',
            name='img_link',
            field=models.ImageField(upload_to='img/media/images/'),
        ),
    ]
