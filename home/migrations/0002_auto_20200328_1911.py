# Generated by Django 2.2.4 on 2020-03-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outcome',
            name='number',
        ),
        migrations.AddField(
            model_name='outcome',
            name='short_description',
            field=models.CharField(default='Option', max_length=50),
            preserve_default=False,
        ),
    ]