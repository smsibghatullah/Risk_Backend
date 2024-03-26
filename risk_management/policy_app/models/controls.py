from django.db import models
from master_app.models.control_objective import ControlObjective
from policy_app.models.policy import Policy, RegulatoryLaws
from master_app.models.department import Department
from django.utils import timezone


from django.db import models

class Control(models.Model):
    description = models.TextField( blank=True)
    responsible_person = models.TextField( blank=True)
    responsible_manager = models.TextField( blank=True)
    departments = models.ManyToManyField(Department,  blank=True)
    control_objective = models.ManyToManyField(ControlObjective,  blank=True)
    policy = models.ManyToManyField(Policy,  blank=True)
    regulatory_laws = models.ManyToManyField(RegulatoryLaws,  blank=True)
    status = models.TextField( blank=True)
    is_critical = models.BooleanField( blank=True)
    issue_reference_number = models.TextField( blank=True)
    issue_creation_date = models.DateField( blank=True,null=True,default=timezone.now)
    assign_to = models.TextField( blank=True)
    assign_to_manager = models.TextField( blank=True)
    short_description = models.TextField( blank=True)
    propose_action_plan = models.TextField( blank=True)
    issue_status = models.TextField( blank=True)





class IssueControl(models.Model):
    issue_reference_number = models.TextField()
    issue_creation_date = models.DateField()
    issue_status = models.TextField() #(Resolved / Open)
    control_objective = models.OneToOneField(ControlObjective, on_delete=models.CASCADE)
    control = models.OneToOneField(Control, on_delete=models.CASCADE)
    assign_to = models.TextField()
    assign_to_manager = models.TextField()
    short_description = models.TextField()
    propose_action_plan = models.TextField()







