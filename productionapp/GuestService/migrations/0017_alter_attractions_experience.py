# Generated by Django 4.1.5 on 2023-01-10 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuestService', '0016_alter_attractions_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractions',
            name='experience',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
    ]
