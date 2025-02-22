# Generated by Django 5.1.6 on 2025-02-18 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img_link', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('study_year', models.CharField(max_length=50)),
                ('total_projects', models.IntegerField()),
                ('total_problems_solved', models.IntegerField()),
                ('total_certifications', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('social_links', models.JSONField()),
                ('resume_link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('img_link', models.CharField(max_length=255)),
                ('live_link', models.CharField(max_length=255)),
                ('github_link', models.CharField(max_length=255)),
                ('tech_stack', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_details', models.JSONField()),
                ('work_experience', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_field', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
    ]
