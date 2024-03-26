from rest_framework import generics
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from master_app.models.department import Department, SubDepartment
from master_app.serializers.department import DepartmentSerializer, SubDepartmentSerializer
from rest_framework import viewsets
from rest_framework import filters


class DepartmentList( generics.ListCreateAPIView):
    search_fields = [ 'name','slug']
    filter_backends = (filters.SearchFilter,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = DepartmentSerializer(queryset, many=True)
    #     # user_groups = []
    #     # for group in request.user.groups.values_list('name', flat=True):
    #     #     user_groups.append(group)
    #     # if 'department' not in user_groups:
    #     #     raise ValidationError('You Dont have permission')
    #     return Response(serializer.data)


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class SubDepartmentList(generics.ListCreateAPIView):
    queryset = SubDepartment.objects.all()
    serializer_class = SubDepartmentSerializer
    region_separator = ","

    def get_queryset(self):
        """
        Optionally restricts the returned articles to given regions,
        by filtering against a `regions` query parameter in the URL.
        """
        departments = self.request.query_params.get("departments", None)
        if departments:
            qs = SubDepartment.objects.filter()
            print(departments.split(self.region_separator))
            qs = qs.filter(department__in=departments.split(self.region_separator))
            return qs
        name_query = self.request.query_params.get("name", None)
        if name_query:
            qs = SubDepartment.objects.filter()
            # print(departments.split(self.region_separator))
            qs = qs.filter(name__contains=name_query)
            return qs

        return super().get_queryset()


class SubDepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubDepartment.objects.all()
    serializer_class = SubDepartmentSerializer
