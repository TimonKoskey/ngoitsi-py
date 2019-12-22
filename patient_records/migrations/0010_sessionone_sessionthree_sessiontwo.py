# Generated by Django 2.2.7 on 2019-12-17 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient_records', '0009_auto_20191213_0701'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('medical_information', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_records.PatientMedicalRecords')),
                ('session', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_records.PatientSession')),
            ],
            options={
                'verbose_name_plural': 'Session Two',
            },
        ),
        migrations.CreateModel(
            name='SessionThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_up_date', models.DateTimeField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('session', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_records.PatientSession')),
            ],
            options={
                'verbose_name_plural': 'Session Three',
            },
        ),
        migrations.CreateModel(
            name='SessionOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_records.PatientPayment')),
                ('session', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_records.PatientSession')),
            ],
            options={
                'verbose_name_plural': 'Session One',
            },
        ),
    ]