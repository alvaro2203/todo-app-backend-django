# Generated by Django 5.0 on 2024-02-01 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_task_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='done',
        ),
    ]