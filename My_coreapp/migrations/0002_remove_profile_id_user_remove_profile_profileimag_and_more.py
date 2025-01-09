# Generated by Django 5.1.4 on 2025-01-07 15:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_coreapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profileimag',
        ),
        migrations.AddField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='profile_images/book-icon.png', upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
