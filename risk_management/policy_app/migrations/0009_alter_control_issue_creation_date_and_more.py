# Generated by Django 4.1.4 on 2023-07-07 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy_app', '0008_alter_control_assign_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='issue_creation_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='issue_reference_number',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='propose_action_plan',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='responsible_manager',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='responsible_person',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='status',
            field=models.TextField(blank=True),
        ),
    ]
