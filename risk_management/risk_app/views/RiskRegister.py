# snippets/views.py
from rest_framework import generics
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from risk_app.models import RiskRegister
from risk_app.serializers.risk_register import RiskRegisterSerializer
from rest_framework import filters



class RiskRegisterList(generics.ListCreateAPIView):
    search_fields = [ 'status','title', 'root_cause', 'inherent_risk_rating_rating', 'overall_control_rating', 'residual_risk_scoring_score']
    filter_backends = (filters.SearchFilter,)
    queryset = RiskRegister.objects.all()
    serializer_class = RiskRegisterSerializer
    def get_queryset(self):
        # department_id = self.kwargs['department_id']
        department_id = None
        if 'department_id' in self.kwargs:
            department_id = self.kwargs['department_id']
        if department_id:
            qs = RiskRegister.objects.filter()
            print(department_id)
            qs = qs.filter(department_id=self.kwargs['department_id'])
            return qs

        parent_id = None
        if 'parent_id' in self.kwargs:
            parent_id = self.kwargs['parent_id']
        if parent_id:
            qs = RiskRegister.objects.filter()
            print(parent_id)
            qs = qs.filter(parent_id=self.kwargs['parent_id'])
            return qs
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
       
        parentonly = self.request.GET.get('parentonly', None)
        queryset = self.filter_queryset(self.get_queryset())
        if parentonly is not None:
            queryset = queryset.filter(parent_id__isnull=True)
            

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ChildRiskRegisterList(generics.ListCreateAPIView):
    search_fields = [ 'status','title', 'root_cause', 'inherent_risk_rating_rating', 'overall_control_rating', 'residual_risk_scoring_score']
    filter_backends = (filters.SearchFilter,)
    queryset = RiskRegister.objects.all()
    serializer_class = RiskRegisterSerializer
    def get_queryset(self):
        # department_id = self.kwargs['department_id']
        department_id = None
        if 'department_id' in self.kwargs:
            department_id = self.kwargs['department_id']
        if department_id:
            qs = RiskRegister.objects.filter()
            qs = qs.filter(department_id=self.kwargs['department_id'])
            return qs

        return super().get_queryset()

    def list(self, request, *args, **kwargs):
       
        parentonly = self.request.GET.get('parentonly', None)
        queryset = self.filter_queryset(self.get_queryset())
        if parentonly is not None:
            queryset = queryset.filter(parent_id__isnull=True)
            

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class RiskRegisterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RiskRegister.objects.all()
    serializer_class = RiskRegisterSerializer
