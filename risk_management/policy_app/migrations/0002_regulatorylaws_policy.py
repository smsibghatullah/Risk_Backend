# Generated by Django 4.1.4 on 2023-04-20 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='regulatorylaws',
            name='policy',
            field=models.ManyToManyField(to='policy_app.policy'),
        ),
    ]
