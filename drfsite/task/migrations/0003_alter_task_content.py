# Generated by Django 5.1.3 on 2024-11-23 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_remove_task_time_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.TextField(),
        ),
    ]