# Generated by Django 4.1.5 on 2023-01-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_student_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]