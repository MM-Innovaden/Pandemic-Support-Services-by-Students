# Generated by Django 2.2.4 on 2020-03-29 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_patient_contacted_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['date_contacted'], 'permissions': (('is_staff', 'Has the staff permissions'),)},
        ),
    ]