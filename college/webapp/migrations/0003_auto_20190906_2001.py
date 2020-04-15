# Generated by Django 2.2.4 on 2019-09-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20190906_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bsc_chem',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='bsc_it',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='bsc_maths',
            name='name',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='bsc_phys',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='civil',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='etc',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='mecha',
            name='name',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='msc_chem',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='msc_maths',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='msc_phys',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='power',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]