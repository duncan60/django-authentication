# Generated by Django 2.1.5 on 2019-02-09 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('versionInfo', '0002_auto_20190208_0127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='draft',
            options={'verbose_name': '草稿管理'},
        ),
        migrations.AlterField(
            model_name='draft',
            name='platform',
            field=models.CharField(choices=[('ios', 'ios'), ('android', 'android')], default='ios', max_length=10, verbose_name='裝置平台'),
        ),
    ]