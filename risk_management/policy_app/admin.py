from django.contrib import admin

from policy_app.models.policy import Policy, RegulatoryLaws
from policy_app.models.controls import Control, IssueControl

admin.site.register(Policy)
admin.site.register(RegulatoryLaws)
admin.site.register(Control)
admin.site.register(IssueControl)