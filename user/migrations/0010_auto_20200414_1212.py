# Generated by Django 3.0.4 on 2020-04-14 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20200409_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slots',
            name='slot_time',
            field=models.TimeField(auto_now=True),
        ),
    ]