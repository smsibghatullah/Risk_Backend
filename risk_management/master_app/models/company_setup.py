from django.db import models
from django.contrib.auth.models import User
from master_app.models.department import Department
from django.contrib.auth.models import Group
Group.add_to_class('key', models.CharField(max_length=180,null=True, blank=True))
User.add_to_class('department', models.CharField(max_length=180,null=True, blank=True))
User.add_to_class('usertype', models.CharField(max_length=30,null=True, blank=True))
User.add_to_class('password_reset_token', models.CharField(max_length=200,null=True, blank=True))



class CompanySetup(models.Model):

    name = models.TextField()
    industry = models.TextField()
    company_domain = models.TextField()
    business_type = models.TextField(null=True, blank=True)
    departments = models.ManyToManyField(Department)
