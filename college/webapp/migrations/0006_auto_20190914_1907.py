# Generated by Django 2.2.4 on 2019-09-14 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_library'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chem',
        ),
        migrations.DeleteModel(
            name='civil',
        ),
        migrations.DeleteModel(
            name='etc',
        ),
        migrations.DeleteModel(
            name='It',
        ),
        migrations.DeleteModel(
            name='Maths',
        ),
        migrations.DeleteModel(
            name='mecha',
        ),
        migrations.DeleteModel(
            name='Phys',
        ),
        migrations.DeleteModel(
            name='Power',
        ),
    ]