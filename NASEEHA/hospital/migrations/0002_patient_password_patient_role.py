# Generated by Django 4.2.1 on 2023-08-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='password',
            field=models.CharField(default='123', max_length=50),
        ),
        migrations.AddField(
            model_name='patient',
            name='role',
            field=models.IntegerField(default=0),
        ),
    ]