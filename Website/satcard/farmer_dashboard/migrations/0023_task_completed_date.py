# Generated by Django 4.1.6 on 2024-04-08 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer_dashboard', '0022_rename_date_task_deadline_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
