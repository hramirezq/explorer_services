# Generated by Django 4.2.1 on 2023-05-10 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliverables',
            old_name='packageId',
            new_name='package_Id',
        ),
    ]
