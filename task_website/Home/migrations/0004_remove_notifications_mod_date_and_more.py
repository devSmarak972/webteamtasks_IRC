# Generated by Django 4.0.6 on 2022-07-17 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_profile_bookmarks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='mod_date',
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='notifications',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='university',
            name='Address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='university',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='university',
            name='Website',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Applications',
            field=models.TextField(blank=True, default='{"applications":[]}', null=True),
        ),
    ]
