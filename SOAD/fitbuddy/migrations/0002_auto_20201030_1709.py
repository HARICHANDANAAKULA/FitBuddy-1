# Generated by Django 3.0.5 on 2020-10-30 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitbuddy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_user',
            new_name='is_customer',
        ),
        migrations.RemoveField(
            model_name='fitnesscenter',
            name='address',
        ),
    ]
