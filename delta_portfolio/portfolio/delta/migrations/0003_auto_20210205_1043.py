# Generated by Django 3.1.3 on 2021-02-05 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0002_db_projects'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='db_projects',
            options={'verbose_name': 'project', 'verbose_name_plural': 'projects'},
        ),
    ]
