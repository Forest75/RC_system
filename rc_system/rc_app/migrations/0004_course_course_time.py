# Generated by Django 2.2.1 on 2019-06-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rc_app', '0003_student_absent_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_time',
            field=models.CharField(default='未知', max_length=50, verbose_name='上课时间'),
        ),
    ]
