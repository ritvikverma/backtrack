# Generated by Django 2.2.6 on 2019-10-24 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backtrack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pbi',
            name='estimate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pbi',
            name='status',
            field=models.CharField(default='Not Yet Started', max_length=50),
        ),
    ]
