from django.db import models
from policy_app.models.policy import Policy

class ControlObjective(models.Model):
    title = models.TextField(default='')
    description = models.TextField()
    responsible_person = models.TextField()
    frequency = models.IntegerField()
    category = models.TextField()
    policy = models.ManyToManyField(Policy)


