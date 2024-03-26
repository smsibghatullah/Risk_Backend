# snippets/views.py
from rest_framework import generics
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import filters
from risk_app.models import RiskAssessment
from risk_app.serializers.risk_assessment import RiskAssessmentSerializer
from django.db.models import Q


class RiskAssessmentList(generics.ListCreateAPIView):
    search_fields = ['category', 'description', 'board_commitee', 'date_of_assessment', 'description', 'executive_management', 'key_risk_indicators', 'risk_appetite_statement', 'risk_appetite', 'risk_tolerance']
    filter_backends = (filters.SearchFilter,)
    queryset = RiskAssessment.objects.all()
    serializer_class = RiskAssessmentSerializer
    def get_queryset(self):
        responisble_department_id = None
        if 'responisble_department_id' in self.kwargs:
            responisble_department_id = self.kwargs['responisble_department_id']
       
        if responisble_department_id:
            qs = RiskAssessment.objects.filter()
            qs = qs.filter(responisble_department_id=self.kwargs['responisble_department_id'])
            return qs
        return super().get_queryset()

class RiskAssessmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RiskAssessment.objects.all()
    serializer_class = RiskAssessmentSerializer

class RiskAssessmentsearch(generics.ListCreateAPIView):
    queryset = RiskAssessment.objects.all()
    serializer_class = RiskAssessmentSerializer

    def get_queryset(self):
        queryset = self.queryset
        search_query = self.request.query_params.get('q', None)
        if search_query is not None:
            query = Q()
            for field in RiskAssessment._meta.fields:
                if field.name == 'id':
                    continue
                lookup = f'{field.name}__icontains'
                query |= Q(**{lookup: search_query})
            queryset = queryset.filter(query)
        return queryset  