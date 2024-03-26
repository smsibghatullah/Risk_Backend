from django.db import models
from django.contrib.auth.models import User
from master_app.models.company_setup import CompanySetup
from master_app.models.department import Department

class RiskPrioritization(models.Model):
   score = models.TextField()
   rating = models.TextField()
   priority = models.TextField()
   color_code = models.TextField()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    company = models.ForeignKey(CompanySetup, on_delete=models.CASCADE, related_name='company')
    departments = models.ManyToManyField(Department)    
class RiskMatrix(models.Model):
   likehood = models.TextField()
   impact = models.TextField()
   combine = models.TextField()
   score = models.TextField()
   likehood_rate = models.TextField()
   impact_rate = models.TextField()
   score_rate = models.TextField()

class ControlRatingMatrix(models.Model):
   design = models.TextField()
   effectiveness = models.TextField()
   formula = models.TextField()
   overall_rating = models.TextField()
   control_score = models.TextField()

class RiskRepo(models.Model):
   title = models.TextField()
   department_id = models.IntegerField(null=True, blank=True)
   description = models.TextField()   
class RiskPlan(models.Model):
   title = models.TextField(max_length=500, blank=False)
   departments = models.TextField(max_length=5000, null=True, blank=True)
class RiskRegister(models.Model):
   department_id = models.IntegerField(null=True, blank=True)
   sub_department = models.TextField(max_length=50, null=True, blank=True)
   file_name = models.CharField(max_length=123, blank=True)
   file = models.FileField(upload_to='Risk_file',null=True, blank=True)
   status = models.CharField(max_length=255)
   title = models.TextField(null=True, blank=True)
   root_cause = models.TextField(null=True, blank=True)
   consequence = models.TextField(null=True, blank=True)
   category = models.TextField(null=True, blank=True)
   function_owner = models.TextField(null=True, blank=True)
   risk_owner = models.TextField(null=True, blank=True)
   risk_champion = models.TextField(null=True, blank=True)
   inherent_risk_rating_likehood = models.TextField(null=True, blank=True)
   inherent_risk_rating_impact = models.TextField(null=True, blank=True)
   inherent_risk_rating_rating = models.TextField(null=True, blank=True)
   control_description = models.TextField(null=True, blank=True)
   control_design_assessement = models.TextField(null=True, blank=True)
   control_effectiveness_assessement = models.TextField(null=True, blank=True)
   overall_control_rating = models.TextField(null=True, blank=True)
   residual_risk_scoring_score = models.TextField(null=True, blank=True)
   risk_responses = models.TextField(null=True, blank=True)
   treatment_required = models.TextField(null=True, blank=True)
   action_plan = models.TextField(null=True, blank=True)
   action_plan_owner = models.TextField(null=True, blank=True)
   implementation_date = models.TextField(null=True, blank=True)  
   parent_id = models.IntegerField(null=True, blank=True)
   previous_assessment = models.TextField(null=True, blank=True)
   updated_at = models.DateField(null=True, blank=True)
   assessment_date = models.DateField(null=True, blank=True)
   next_review_date = models.DateField(null=True, blank=True)
   review_status = models.TextField(null=True, blank=True, default='Draft',)

class RiskAssessment(models.Model):
   category = models.TextField(null=True, blank=True)
   risk_appetite_statement = models.TextField(null=True, blank=True)
   description = models.TextField(null=True, blank=True)
   responisble_department_id = models.TextField(null=True, blank=True)
   key_risk_indicators = models.TextField(null=True, blank=True)
   risk_appetite = models.TextField(null=True, blank=True)
   date_of_assessment = models.TextField(null=True, blank=True)
   kri_reporting = models.TextField(null=True, blank=True)
   previous_assessment = models.TextField(null=True, blank=True)
