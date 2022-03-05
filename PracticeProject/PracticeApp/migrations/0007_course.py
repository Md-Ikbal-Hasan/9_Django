# Generated by Django 4.0.2 on 2022-02-23 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PracticeApp', '0006_department_department_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('students', models.ManyToManyField(to='PracticeApp.Student')),
            ],
        ),
    ]
