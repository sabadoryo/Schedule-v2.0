# Generated by Django 3.0.5 on 2020-04-17 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule3', '0016_remove_event_bg_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='color',
            field=models.CharField(default='', max_length=200),
        ),
    ]
