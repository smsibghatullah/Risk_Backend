# snippets/views.py
from rest_framework import generics
from rest_framework import filters
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from risk_app.models import RiskPrioritization
from risk_app.serializers.risk_prioritization import RiskPrioritizationSerializer



class RiskPrioritizationList(generics.ListCreateAPIView):
    search_fields = ['score', 'rating', 'priority', 'color_code']
    ordering_fields = ['score', 'rating', 'priority', 'color_code']
    filter_backends = (filters.SearchFilter,)
    queryset = RiskPrioritization.objects.all()
    serializer_class = RiskPrioritizationSerializer
    def list(self, request):
        queryset = self.get_queryset()
        serializer = RiskPrioritizationSerializer(queryset, many=True)
        user_groups = []
        for group in request.user.groups.values_list('name', flat=True):
            user_groups.append(group)
        if 'risk_prioritization' not in user_groups:
            raise ValidationError('You have already signed up')
        return Response(serializer.data) 

class RiskPrioritizationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RiskPrioritization.objects.all()
    serializer_class = RiskPrioritizationSerializer
