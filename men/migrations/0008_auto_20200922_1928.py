# Generated by Django 3.1 on 2020-09-23 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0007_auto_20200922_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='display',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='display',
            name='desc',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='display',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
