# Generated by Django 3.0.5 on 2020-04-17 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule3', '0017_subjects_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='modal_page',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]
