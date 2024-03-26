# snippets/urls.py
from django.urls import path
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
# from risk_app.views.companysetups import CompanysetupList, CompanysetupDetail
from risk_app.views.ControlRatingMatrix import ControlRatingMatrixList, ControlRatingMatrixDetail
# from risk_app.views.Department import DepartmentList, DepartmentDetail
from risk_app.views.Profile import ProfileList, ProfileDetail
from risk_app.views.RiskAssessment import RiskAssessmentDetail, RiskAssessmentList,RiskAssessmentsearch
from risk_app.views.RiskMatrix import RiskMatrixList, RiskMatrixDetail
from risk_app.views.RiskPrioritization import RiskPrioritizationList, RiskPrioritizationDetail
from risk_app.views.RiskRegister import RiskRegisterList, RiskRegisterDetail, ChildRiskRegisterList
from risk_app.views.RiskRepo import RiskRepoDetail, RiskRepoList,RiskRepoSearch


urlpatterns = [
    path('control_rating_matrix/', ControlRatingMatrixList.as_view()),
    path('control_rating_matrix/<int:pk>/', ControlRatingMatrixDetail.as_view()),
    path('profile/', ProfileList.as_view()),
    path('profile/<int:pk>/', ProfileDetail.as_view()),
    path('risk_matrix/', RiskMatrixList.as_view()),
    path('risk_matrix/<int:pk>/', RiskMatrixDetail.as_view()),
    path('risk_prioritization/', RiskPrioritizationList.as_view()),
    path('risk_prioritization/<int:pk>/', RiskPrioritizationDetail.as_view()),

    path('all_risk/', RiskRegisterList.as_view()),
    path('all_child_risk/', ChildRiskRegisterList.as_view()),
    path('all_risk/<int:parent_id>', RiskRegisterList.as_view()),
    path('risk_register/', RiskRegisterList.as_view()),
    # path('risk_register/<int:department_id>', RiskRegisterList.as_view()),
    path('risk_register/department_id/<int:department_id>', RiskRegisterList.as_view()),
    path('risk_register/<int:pk>/', RiskRegisterDetail.as_view()),

    path('risk_repo/', RiskRepoList.as_view()),
    path('risk_repo/search/', RiskRepoSearch.as_view()),
    path('risk_repo/<int:department_id>', RiskRepoList.as_view()),
    path('risk_repo/<int:pk>/', RiskRepoDetail.as_view()),

    path('risk_assessment/', RiskAssessmentList.as_view()),
    path('risk_assessment/departments/<int:responisble_department_id>', RiskAssessmentList.as_view()),
    path('risk_assessment/<int:pk>/', RiskAssessmentDetail.as_view()),
    path('risk_assessment/search/', RiskAssessmentsearch.as_view()),
]
