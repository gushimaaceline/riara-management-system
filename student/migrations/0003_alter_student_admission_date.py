# Generated by Django 3.2.3 on 2021-09-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_date',
            field=models.DateField(null=True),
        ),
    ]