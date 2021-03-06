# Generated by Django 2.2.7 on 2019-12-17 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient_records', '0010_sessionone_sessionthree_sessiontwo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientsession',
            name='doctor_session',
        ),
        migrations.RemoveField(
            model_name='patientsession',
            name='follow_up_date',
        ),
        migrations.RemoveField(
            model_name='patientsession',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='sessionone',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='sessiontwo',
            name='medical_information',
        ),
        migrations.AddField(
            model_name='patientmedicalrecords',
            name='session',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_records.SessionTwo'),
        ),
        migrations.AddField(
            model_name='patientpayment',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_records.SessionOne'),
        ),
    ]
