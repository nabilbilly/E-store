# Generated by Django 5.0.6 on 2024-06-10 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Useraccount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
