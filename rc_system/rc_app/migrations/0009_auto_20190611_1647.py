# Generated by Django 2.2.2 on 2019-06-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rc_app', '0008_studentabsentsituation_absent_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentabsentsituation',
            name='absent_time',
            field=models.DateTimeField(verbose_name='缺勤时间'),
        ),
    ]