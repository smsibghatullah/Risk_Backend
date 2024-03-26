from django.contrib import admin

from master_app.models.company_setup import CompanySetup
from master_app.models.department import Department, SubDepartment

admin.site.register(CompanySetup)
admin.site.register(SubDepartment)
admin.site.register(Department)
