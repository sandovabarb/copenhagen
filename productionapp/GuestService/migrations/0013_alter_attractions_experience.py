# Generated by Django 4.1.5 on 2023-01-10 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuestService', '0012_attractions_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractions',
            name='experience',
            field=models.CharField(default='not thinking anything yet', max_length=2000),
        ),
    ]
