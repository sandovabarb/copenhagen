# Generated by Django 4.1.5 on 2023-01-10 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuestService', '0014_alter_attractions_image_of_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractions',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='GuestService/static'),
        ),
    ]
