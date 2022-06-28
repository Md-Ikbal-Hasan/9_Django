# Generated by Django 4.0.4 on 2022-06-02 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('birthday', models.DateField()),
                ('job_position', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=20)),
                ('cover_letter', models.TextField()),
                ('cv', models.FileField(max_length=250, upload_to=None)),
            ],
        ),
    ]