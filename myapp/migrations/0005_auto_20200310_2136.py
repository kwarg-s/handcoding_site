# Generated by Django 2.1.3 on 2020-03-10 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_screen_gaming_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='screen',
            name='day',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='screen',
            name='day_problem',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='screen',
            name='problem',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='screen',
            name='user',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='screen',
            name='gaming',
            field=models.IntegerField(default=-1),
        ),
    ]