# Generated by Django 4.2.1 on 2023-08-16 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_hospital_information_specialization_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userp',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email address',blank= False, null=True, unique= True),
        ),
        migrations.AlterField(
            model_name='userp',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
