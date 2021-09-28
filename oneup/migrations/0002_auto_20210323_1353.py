# Generated by Django 3.1.3 on 2021-03-23 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logname', models.CharField(blank=True, max_length=50, null=True)),
                ('logsn', models.CharField(blank=True, max_length=50, null=True)),
                ('wh', models.CharField(blank=True, max_length=50, null=True)),
                ('dis', models.CharField(blank=True, max_length=50, null=True)),
                ('agen', models.CharField(blank=True, max_length=50, null=True)),
                ('logcustom', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='as',
            old_name='date',
            new_name='asdate',
        ),
        migrations.RenameField(
            model_name='manufacture',
            old_name='date',
            new_name='mfdate',
        ),
        migrations.RenameField(
            model_name='outsourcing',
            old_name='date',
            new_name='osdate',
        ),
        migrations.RemoveField(
            model_name='as',
            name='name',
        ),
        migrations.RemoveField(
            model_name='manufacture',
            name='history',
        ),
        migrations.RemoveField(
            model_name='manufacture',
            name='sn',
        ),
        migrations.RemoveField(
            model_name='manufacture',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='outsourcing',
            name='serial',
        ),
        migrations.RemoveField(
            model_name='outsourcing',
            name='status',
        ),
        migrations.AddField(
            model_name='as',
            name='asname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='as',
            name='assta',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='as',
            name='record',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='halfpro',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='mfsn',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='mfsta',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='origin',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='workercode',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='outsourcing',
            name='osqu',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='outsourcing',
            name='ossn',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='as',
            name='pronumber',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='manufacture',
            name='proname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]