# Generated by Django 3.1.3 on 2020-11-09 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('device', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='devices.device')),
            ],
            options={
                'verbose_name': 'Action',
                'verbose_name_plural': 'Actions',
                'db_table': 'actions',
            },
        ),
    ]
