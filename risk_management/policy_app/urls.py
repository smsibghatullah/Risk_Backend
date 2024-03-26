# snippets/urls.py
from django.urls import path
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token


from policy_app.views.policy import PolicyList, PolicyDetail, RegulatoryLawsList, RegulatoryLawsDetail, PolicyRegulatoryLawsList,PolicyDepartment,Policysearch,RegulatoryLawssearch
from policy_app.views.control import ControlList, ControlDetail, IssueControlList, IssueControlDetail, PolicyControlObjectiveList,Controlsearch


urlpatterns = [
    path('policy/', PolicyList.as_view()),
    path('policy/<int:pk>/', PolicyDetail.as_view()),
    path('policy/department/', PolicyDepartment.as_view()),
    path('policy/department/<int:departments>', PolicyDepartment.as_view()),
     path('policy/search/', Policysearch.as_view()),
   
    path('control/', ControlList.as_view()),
    path('control/policy/', PolicyControlObjectiveList.as_view()),
    path('control/<int:pk>/', ControlDetail.as_view()),
     path('control/search/', Controlsearch.as_view()),


    path('issue_control/', IssueControlList.as_view()),
    path('issue_control/<int:pk>/', IssueControlDetail.as_view()),


    path('regulatory_law/', RegulatoryLawsList.as_view()),
    path('regulatory_law/<int:pk>/', RegulatoryLawsDetail.as_view()),
    path('controlObject/policy/', PolicyControlObjectiveList.as_view()),
    path('regulatory_laws/policy/', PolicyRegulatoryLawsList.as_view()),
    path('regulatory_law/search/', RegulatoryLawssearch.as_view()),

]
