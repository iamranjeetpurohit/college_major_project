# Generated by Django 2.2.4 on 2019-10-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_auto_20191008_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='files',
            field=models.ImageField(blank=True, default='', null=True, upload_to='notice/files'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='notice/images'),
        ),
    ]