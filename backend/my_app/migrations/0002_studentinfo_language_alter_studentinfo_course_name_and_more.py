# Generated by Django 5.1.8 on 2025-04-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='language',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Student language'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='course_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Course Name'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='student_chat_id',
            field=models.BigIntegerField(blank=True, null=True, unique=True, verbose_name='Student Chat ID'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='teacher_course_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="Teacher's Course Name"),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='teacher_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Teacher Name'),
        ),
    ]
