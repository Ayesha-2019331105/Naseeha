# Generated by Django 4.2.1 on 2023-08-23 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0011_alter_hospital_department_hospital_department_name_and_more'),
        ('doctors', '0005_remove_doctor_info_specialization'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor_info')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('appointment_date', models.DateField(blank=True, null=True)),
                ('appointment_time', models.TimeField(blank=True, null=True)),
                ('appointment_status', models.CharField(blank=True, default='Pending', max_length=70, null=True)),
                ('serial_number', models.IntegerField(blank=True, default=0, null=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor_info')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
    ]
