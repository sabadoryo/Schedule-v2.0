# Generated by Django 3.0.5 on 2020-04-16 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule3', '0013_auto_20200416_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='modal_page',
            field=models.CharField(default='', max_length=200),
        ),
    ]
