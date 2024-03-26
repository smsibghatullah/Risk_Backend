from django.contrib import admin


from risk_app.models import ControlRatingMatrix
# from risk_app.models import Department
from risk_app.models import Profile
from risk_app.models import RiskMatrix
from risk_app.models import RiskPrioritization
from risk_app.models import RiskRegister


admin.site.register(ControlRatingMatrix)
# admin.site.register(Department)
admin.site.register(Profile)
admin.site.register(RiskMatrix)
admin.site.register(RiskPrioritization)
admin.site.register(RiskRegister)


# Register your models here.
