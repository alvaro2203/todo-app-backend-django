# Generated by Django 5.0 on 2024-02-01 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_alter_task_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('pending', 'pending'), ('doing', 'doing'), ('done', 'done')], default='pending', max_length=10),
        ),
    ]
