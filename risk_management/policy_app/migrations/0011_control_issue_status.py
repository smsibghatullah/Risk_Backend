# Generated by Django 4.1.4 on 2023-07-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy_app', '0010_alter_control_issue_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='control',
            name='issue_status',
            field=models.TextField(blank=True),
        ),
    ]
