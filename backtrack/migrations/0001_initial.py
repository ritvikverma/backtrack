# Generated by Django 2.2.6 on 2019-11-07 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PBI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('priority', models.IntegerField()),
                ('status', models.CharField(default='Not Yet Started', max_length=50)),
                ('story_points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('effort_hours', models.IntegerField()),
                ('developer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backtrack.Person')),
                ('pbi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backtrack.PBI')),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('capacity', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backtrack.Project')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backtrack.Project'),
        ),
        migrations.AddField(
            model_name='pbi',
            name='project_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backtrack.Project'),
        ),
        migrations.AddField(
            model_name='pbi',
            name='sprint_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backtrack.Sprint'),
        ),
    ]
