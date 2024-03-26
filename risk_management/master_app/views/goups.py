from rest_framework import generics
from django.contrib.auth.models import Group, Permission

from django.core.exceptions import ValidationError
from rest_framework.response import Response
# from master_app.models.department import Department, SubDepartment
from master_app.serializers.group import GroupSerializer, PermissionSerializer


class GroupList( generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PermissionList( generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
   
    def get_queryset(self):
            qs = Permission.objects.filter()
            # print(departments.split(self.region_separator))
            name_query = 'custom'
            qs = qs.filter(name__contains=name_query)
            return qs

class PermissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
