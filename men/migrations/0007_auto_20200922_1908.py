# Generated by Django 3.1 on 2020-09-23 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0006_display3_bdgd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='display',
            name='title',
            field=models.CharField(max_length=600),
        ),
    ]
