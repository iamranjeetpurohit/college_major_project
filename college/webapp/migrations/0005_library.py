# Generated by Django 2.2.4 on 2019-09-06 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20190906_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('qualification', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('number', models.CharField(default='N/A', max_length=15)),
            ],
        ),
    ]
