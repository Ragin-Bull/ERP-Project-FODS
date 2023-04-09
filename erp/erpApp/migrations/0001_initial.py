# Generated by Django 4.2 on 2023-04-08 05:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import erpApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=50)),
                ('credits_score', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('semester', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentName', models.CharField(max_length=100)),
                ('facId', models.IntegerField()),
                ('depCode', models.CharField(max_length=2, validators=[erpApp.models.depError])),
            ],
        ),
        migrations.CreateModel(
            name='Enrollments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=2)),
                ('courseData', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='erpApp.course')),
                ('studentData', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='users.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='deptId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dept', to='erpApp.department'),
        ),
    ]