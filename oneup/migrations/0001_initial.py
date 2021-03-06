# Generated by Django 3.1.3 on 2021-03-22 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='As',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ph', models.CharField(max_length=50)),
                ('pronumber', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proname', models.CharField(max_length=30)),
                ('sn', models.CharField(max_length=30)),
                ('history', models.CharField(max_length=50)),
                ('stock', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Outsourcing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
