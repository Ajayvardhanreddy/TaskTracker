# Generated by Django 4.0.3 on 2022-03-13 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=100)),
                ('task_name', models.CharField(max_length=100)),
                ('priority', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('team_member', models.CharField(max_length=100)),
                ('task_status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TeamsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.CharField(max_length=100)),
                ('team_name', models.CharField(max_length=100)),
                ('team_member_id', models.CharField(max_length=100)),
                ('status_of_member', models.BooleanField()),
            ],
        ),
    ]
