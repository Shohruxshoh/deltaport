# Generated by Django 3.1.3 on 2021-02-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefon', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
            ],
        ),
    ]
