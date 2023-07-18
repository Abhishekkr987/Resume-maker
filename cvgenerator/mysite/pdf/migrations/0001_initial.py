# Generated by Django 4.2.1 on 2023-05-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('pin_code', models.IntegerField(max_length=6)),
                ('city', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=15)),
                ('marital_status', models.CharField(max_length=40)),
                ('linked_in', models.CharField(default='', max_length=20)),
                ('website', models.CharField(default='', max_length=20)),
                ('description', models.CharField(max_length=250)),
                ('job_title', models.CharField(max_length=100)),
                ('job_city', models.CharField(max_length=50)),
                ('job_company', models.CharField(max_length=50)),
                ('job_start_month', models.CharField(max_length=15)),
                ('job_start_year', models.IntegerField(max_length=4)),
                ('job_end_month', models.CharField(max_length=15)),
                ('job_end_year', models.IntegerField(max_length=4)),
                ('job_description', models.CharField(max_length=400)),
                ('edu_degree', models.CharField(max_length=50)),
                ('edu_city', models.CharField(max_length=15)),
                ('edu_university', models.CharField(max_length=100)),
                ('edu_school', models.CharField(max_length=25)),
                ('edu_degree_end_month', models.CharField(max_length=15)),
                ('edu_degree_end_year', models.IntegerField(max_length=4)),
                ('edu_degree_description', models.CharField(max_length=500)),
                ('skills', models.CharField(max_length=1000)),
                ('hobby', models.CharField(max_length=500)),
            ],
        ),
    ]
