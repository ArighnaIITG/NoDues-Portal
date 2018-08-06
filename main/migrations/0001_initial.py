# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-12 14:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'Account', max_length=250)),
                ('webmail', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='asstreg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('webmail', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Caretaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('webmail', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=250)),
                ('hostel', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'CC', max_length=250)),
                ('webmail', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('webmail', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=250)),
                ('dept', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gymkhana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'Gymkhana', max_length=250)),
                ('webmail', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='HOD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('webmail', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=250)),
                ('dept', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'Lab', max_length=250)),
                ('webmail', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'Library', max_length=250)),
                ('webmail', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('roll', models.IntegerField(default=0)),
                ('webmail', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=250)),
                ('dept', models.CharField(max_length=100)),
                ('hostel', models.CharField(max_length=100)),
                ('caretaker_approval', models.BooleanField(default=False)),
                ('warden_approval', models.BooleanField(default=False)),
                ('gymkhana_approval', models.BooleanField(default=False)),
                ('library_approval', models.BooleanField(default=False)),
                ('CC_approval', models.BooleanField(default=False)),
                ('asstreg_approval', models.BooleanField(default=False)),
                ('HOD_approval', models.BooleanField(default=False)),
                ('account_approval', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StudFacStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Faculty')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Student')),
            ],
        ),
        migrations.CreateModel(
            name='StudLabStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Lab')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Warden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('webmail', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=250)),
                ('hostel', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='faculty_approval',
            field=models.ManyToManyField(through='main.StudFacStatus', to='main.Faculty'),
        ),
        migrations.AddField(
            model_name='student',
            name='lab_approval',
            field=models.ManyToManyField(through='main.StudLabStatus', to='main.Lab'),
        ),
    ]
