# Generated by Django 2.2.7 on 2019-11-28 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient_records', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientdetails',
            old_name='date_updated',
            new_name='last_updated',
        ),
    ]
