# Generated by Django 4.1.4 on 2023-05-27 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit_app', '0005_observations_auditprogram_agree_date_action_plan_and_more'),
    ]

    operations = [
      #  migrations.AddField(
       #     model_name='auditprogram',
        #    name='agree_date_action_plan',
         #   field=models.DateField(blank=True, null=True),
       # ),
  #      migrations.AddField(
   #         model_name='auditprogram',
    #        name='approval_status',
     #       field=models.TextField(blank=True, default='created'),
      #  ),
        migrations.AlterField(
            model_name='auditengagement',
            name='state',
            field=models.CharField(blank=True, default='Draft', max_length=30),
        ),
    ]
