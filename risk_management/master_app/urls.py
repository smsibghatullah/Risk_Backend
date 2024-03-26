# snippets/urls.py
from django.urls import path
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from master_app.views.companysetups import CompanySetupList, CompanySetupDetail
from master_app.views.Department import DepartmentList, DepartmentDetail,SubDepartmentList, SubDepartmentDetail
from master_app.views.user import RegisterAPI, UpdateUser, UserList, UserDetail,Usersearch
from master_app.views.goups import GroupList, GroupDetail, PermissionDetail, PermissionList
from master_app.views.control_objective import ControlObjectiveList, ControlObjectiveDetail,ControlObjectiveSeach, TodoListApiView
from master_app.views.CustomAuthToken import CustomAuthToken
from master_app.views.forgotAuth import ForgotPasswordView, ResetPasswordView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('controlobjective/', ControlObjectiveList.as_view()),
    path('controlobjective/<int:pk>/', ControlObjectiveDetail.as_view()),
    path('controlobjective/search/', ControlObjectiveSeach.as_view()),

    path('companysetup/', CompanySetupList.as_view()),
    path('companysetup/<int:pk>/', CompanySetupDetail.as_view()),

    path('department/', DepartmentList.as_view()),
    path('department/<int:pk>/', DepartmentDetail.as_view()),
    path('subdepartment/', SubDepartmentList.as_view()),
    path('subdepartment/<int:pk>/', SubDepartmentDetail.as_view()),

    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),  # <-- And here
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('user/', UserList.as_view()),
    path('user/update/<int:pk>', UpdateUser.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
    path('user/search/', Usersearch.as_view()),
    path('group/', GroupList.as_view()),
    path('group/<int:pk>/', GroupDetail.as_view()),
    path('permission/', PermissionList.as_view()),
    path('permission/<int:pk>/', PermissionDetail.as_view()),

    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('comment', TodoListApiView.as_view()),
]
