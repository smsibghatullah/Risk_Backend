# Generated by Django 4.1.4 on 2023-04-06 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit_app', '0003_auditprogram_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditprogram',
            name='implications',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='auditprogram',
            name='our_description',
            field=models.TextField(blank=True),
        ),
    ]
