# Generated by Django 3.1.3 on 2021-02-16 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0003_auto_20210205_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html', models.IntegerField(max_length=100)),
                ('css', models.IntegerField(max_length=100)),
                ('python', models.IntegerField(max_length=100)),
            ],
            options={
                'verbose_name': 'skill',
                'verbose_name_plural': 'skills',
            },
        ),
    ]
