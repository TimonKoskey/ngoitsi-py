# Generated by Django 2.2.7 on 2019-12-02 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_records', '0002_auto_20191128_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdetails',
            name='age',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
