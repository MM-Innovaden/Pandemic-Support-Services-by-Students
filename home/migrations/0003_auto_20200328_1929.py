# Generated by Django 2.2.4 on 2020-03-28 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200328_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outcome',
            name='short_description',
        ),
        migrations.AlterField(
            model_name='outcome',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]
