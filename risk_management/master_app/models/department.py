from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
   name = models.TextField()
   slug = models.TextField()


class SubDepartment(models.Model):
   name = models.TextField()
   slug = models.TextField()
   department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department')

class DocComment(models.Model):
   belogTo = models.TextField()
   docId = models.TextField()
   comment = models.TextField()
   


