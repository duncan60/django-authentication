# Generated by Django 2.1.5 on 2019-02-11 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('versionInfo', '0010_auto_20190211_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='draft',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='versionInfo.Draft', verbose_name='審核內容'),
        ),
    ]