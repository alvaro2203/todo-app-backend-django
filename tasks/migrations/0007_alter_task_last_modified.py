# Generated by Django 5.0 on 2024-02-01 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
