# Generated by Django 2.1.5 on 2019-02-07 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('versionInfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='updateinfo',
            name='update_text',
            field=models.TextField(default='', max_length=200),
        ),
    ]
