# Generated by Django 3.1.3 on 2021-02-17 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0005_auto_20210216_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefon', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('adress', models.CharField(max_length=100)),
            ],
        ),
    ]
