# Generated by Django 5.0.6 on 2024-08-18 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nika', '0004_projects_alter_visitor_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='github_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
