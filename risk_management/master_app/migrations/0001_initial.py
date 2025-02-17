# Generated by Django 4.1.4 on 2023-06-08 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanySetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('industry', models.TextField()),
                ('company_domain', models.TextField()),
                ('business_type', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ControlObjective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('responsible_person', models.TextField()),
                ('frequency', models.IntegerField()),
                ('category', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('slug', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DocComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belogTo', models.TextField()),
                ('docId', models.TextField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SubDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('slug', models.TextField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='master_app.department')),
            ],
        ),
    ]
