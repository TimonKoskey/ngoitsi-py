# Generated by Django 2.2.7 on 2019-11-27 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_number', models.IntegerField(blank=True, null=True)),
                ('surname', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sex', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=50, null=True)),
                ('county', models.CharField(blank=True, max_length=50, null=True)),
                ('sub_county', models.CharField(blank=True, max_length=50, null=True)),
                ('village_or_estate', models.CharField(blank=True, max_length=50, null=True)),
                ('post_code', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'PatientDetails',
            },
        ),
        migrations.CreateModel(
            name='PatientPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(blank=True, max_length=50, null=True)),
                ('amount', models.CharField(blank=True, max_length=50, null=True)),
                ('patient_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_records.PatientDetails')),
            ],
        ),
        migrations.CreateModel(
            name='PatientMedicalRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaints', models.CharField(blank=True, max_length=1000, null=True)),
                ('investigations', models.CharField(blank=True, max_length=1000, null=True)),
                ('treatment', models.CharField(blank=True, max_length=1000, null=True)),
                ('visit_date', models.DateTimeField(auto_now_add=True)),
                ('follow_up_date', models.DateTimeField(blank=True, null=True)),
                ('patient_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_records.PatientDetails')),
            ],
        ),
    ]
