# Generated by Django 4.1.5 on 2023-01-10 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuestService', '0008_alter_attractions_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractions',
            name='image',
            field=models.ImageField(default='', upload_to='GuestService/images'),
        ),
    ]
