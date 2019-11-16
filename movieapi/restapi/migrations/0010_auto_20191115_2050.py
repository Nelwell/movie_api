# Generated by Django 2.2.5 on 2019-11-16 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0009_auto_20191113_1901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiclemaintenance',
            old_name='task',
            new_name='location',
        ),
        migrations.AddField(
            model_name='vehiclemaintenance',
            name='service',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
