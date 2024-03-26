
from django.db import models
from master_app.models.company_setup import CompanySetup
from master_app.models.department import Department, SubDepartment
from risk_app.models import RiskRegister
from policy_app.models.controls import Control


class AnnualPlan(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=500, blank=True)
    departments = models.TextField(max_length=5000, null=True, blank=True)
    state = models.CharField(max_length=30, blank=True, default='Draft')
    start_date=models.DateField(null=True, blank=True)
    end_date=models.DateField(null=True, blank=True)
    file_name = models.CharField(max_length=123,blank=True)
    file = models.FileField(upload_to='Audit_Plan_File',blank=True)
    approved_commit=models.CharField(max_length=500,blank=True)
    # 
    

class AuditEngagement(models.Model):

    name = models.TextField(max_length=500, blank=True)
    allocated_manager = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True, default='Draft')
    annual_plan = models.ForeignKey(AnnualPlan, on_delete=models.CASCADE, related_name='annual_plan')
    # subdepartment = models.ForeignKey(SubDepartment, on_delete=models.CASCADE, related_name='subdepartment')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='departmentId')
    duration_days = models.CharField(max_length=30, blank=True)
    duration_hours = models.CharField(max_length=30, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)
    objective = models.TextField(max_length=500, blank=True)
    description_approval = models.TextField(blank=True)
    department_head=models.TextField(max_length=500,blank=True)
    total_staff=models.TextField(max_length=500,blank=True)
    approved_policies=models.TextField(max_length=500,blank=True)
    audit_observation=models.TextField(max_length=500,blank=True)
    open_issues=models.TextField(max_length=500,blank=True)
    # audit_program = models.ManyToManyField(AuditProgram, null=True, blank=True)
    #     

# Audit Program Screen
class AuditProgram(models.Model):

    category = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    title_of_procedure =  models.TextField(blank=True)
    summary_of_procedure =  models.TextField(blank=True)
    design_assessment_result =  models.TextField(blank=True) # only two value 'effective,'non effective'
    operating_assessment_result =  models.TextField(blank=True) # only two value 'effective,'non effective'
    audit_process_result =  models.TextField(blank=True) # only two value 'Satisfactory,'Unsatisfactory'
    issue_check=models.BooleanField(blank=True,default=False)
    audit_engagement = models.ForeignKey(AuditEngagement, on_delete=models.CASCADE, related_name='aduit_engagment_program', blank=True,default=False)
    risk_tagging = models.ManyToManyField(RiskRegister,blank=True)
    control_issue= models.TextField(blank=True)
    action_plan=models.CharField(max_length=300,blank=True)
    our_reputation=models.TextField(null=True, blank=True)
    our_observation=models.CharField(max_length=300,blank=True)
    management_response=models.CharField(max_length=300,blank=True)
    implications=models.CharField(max_length=300,blank=True)
    controls =models.ManyToManyField(Control,blank=True)
    approval_status = models.TextField(blank=True,default='Draft')
    agree_date_action_plan = models.DateField(null=True, blank=True)
    

class AuditProgramAttachment(models.Model):
    file_name = models.CharField(max_length=123,blank=True)
    content = models.FileField(upload_to='audit_files')
    auditprogram = models.ForeignKey(AuditProgram, related_name="auditengagement_attachment", on_delete=models.CASCADE,)

class AuditEngagementAttachment(models.Model):
    file_name = models.CharField(max_length=123,blank=True)
    content = models.FileField(upload_to='audit_files')
    ticket = models.ForeignKey(AuditEngagement, related_name="auditengagement_attachment", on_delete=models.CASCADE,)


class AuditProgramRepo(models.Model):
    title = models.TextField()
    summary = models.TextField(null=True, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)

