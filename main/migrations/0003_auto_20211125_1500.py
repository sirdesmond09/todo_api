# Generated by Django 3.2.8 on 2021-11-25 14:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_todo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='todo',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]