# Generated by Django 4.1.6 on 2023-10-29 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer_dashboard', '0006_alter_croptype_icon_alter_croptype_wms_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='static/farmer_dashboard/assets/farmers_photo/'),
        ),
    ]
