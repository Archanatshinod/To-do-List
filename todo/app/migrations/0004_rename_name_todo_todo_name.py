# Generated by Django 5.0.6 on 2024-06-26 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='name',
            new_name='Todo_name',
        ),
    ]