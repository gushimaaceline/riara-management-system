# Generated by Django 3.2.3 on 2021-08-20 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20)),
                ('course_code', models.CharField(max_length=20)),
                ('trainer_id', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('syllabus', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
    ]