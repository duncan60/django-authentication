# Generated by Django 2.1.5 on 2019-02-07 14:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('versionInfo', '0003_auto_20190207_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft',
            name='platform',
            field=models.CharField(choices=[('IOS', 'ios'), ('ANDROID', 'android')], default='IOS', max_length=20),
        ),
        migrations.AddField(
            model_name='updateinfo',
            name='platform',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='draft',
            name='version',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='updateinfo',
            name='version',
            field=models.CharField(max_length=10),
        ),
    ]