from django.contrib import admin
# Register your models here.
from audit_app.models.annual_plan import AnnualPlan, AuditEngagement,AuditProgram,AuditProgramRepo

admin.site.register(AnnualPlan)
admin.site.register(AuditEngagement)
admin.site.register(AuditProgram)
admin.site.register(AuditProgramRepo)