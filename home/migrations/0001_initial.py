# Generated by Django 2.2.4 on 2020-03-28 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.PositiveSmallIntegerField()),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=10)),
                ('date_contacted', models.DateField()),
                ('outcome', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='home.Outcome')),
            ],
            options={
                'ordering': ['date_contacted'],
            },
        ),
    ]
