# Generated by Django 3.1.3 on 2021-02-16 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0004_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='css',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skills',
            name='html',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skills',
            name='python',
            field=models.IntegerField(),
        ),
    ]
