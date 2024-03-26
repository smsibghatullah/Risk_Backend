from django.db import models
from master_app.models.department import Department
from django.utils import timezone


class Policy(models.Model):

    
    name = models.TextField(max_length=500, blank=False)
    departments = models.ManyToManyField(Department)
    owner = models.CharField(max_length=30, blank=False)
    state = models.CharField(max_length=30, blank=False, default='Draft')
    file_name = models.CharField(max_length=123,blank=True)
    file = models.FileField(upload_to='policy_file',blank=True)
    date_approval = models.DateField( default=timezone.now)
    policy_edit = models.TextField(blank=True)
    policy_text = models.TextField(max_length=500,blank=False)
    review_date = models.DateField(default=timezone.now)
    
class RegulatoryLaws(models.Model):

    name = models.TextField(max_length=500, blank=False)
    departments = models.ManyToManyField(Department)
    owner = models.CharField(max_length=30, blank=False)
    state = models.CharField(max_length=30, blank=False, default='Draft')
    file_name = models.CharField(max_length=123)
    file = models.FileField(upload_to='regulatory_law_file', blank=True)
    policy = models.ManyToManyField(Policy)

