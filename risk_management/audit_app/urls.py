# snippets/urls.py
from django.urls import path
from audit_app.views.annual_plan import AnnualPlanList, AnnualPlanDetail, AuditEngagementDetail, AuditEngagementList, \
    AuditEngagementAttachmentList, AuditEngagementAttachmentDetail, AuditProgramRepoList, AuditProgramRepoDetail,\
    AuditProgramList, AuditProgramDetail,AnnualPlansearch,AuditProgramRepoSearch,AuditEngagementsearch,AuditProgramSearch,\
    AuditProgramAttachmentList

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('annualplan/', AnnualPlanList.as_view()),
    path('annualplan/<int:pk>/', AnnualPlanDetail.as_view()),
     path('annualplan/search/', AnnualPlansearch.as_view()),

    path('audit_program_repo/', AuditProgramRepoList.as_view()),
    path('audit_program_repo/search/', AuditProgramRepoSearch.as_view()),
    path('audit_program_repo/<int:pk>/', AuditProgramRepoDetail.as_view()),

    path('audit_program/', AuditProgramList.as_view()),
    path('audit_program/search/', AuditProgramSearch.as_view()),
    path('audit_program/audit_engagement/<int:audit_engagement>', AuditProgramList.as_view()),

    path('audit_program/<int:pk>/', AuditProgramDetail.as_view()),

    path('auditengagement/', AuditEngagementList.as_view()),
    path('auditengagement/<int:pk>/', AuditEngagementDetail.as_view()),
    path('auditengagement/search/', AuditEngagementsearch.as_view()),

    path('auditengagement_attachment/', AuditEngagementAttachmentList.as_view()),
    path('auditengagement_attachment/<int:pk>/', AuditEngagementAttachmentDetail.as_view()),

    path('auditprogram_attachment/', AuditProgramAttachmentList.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
