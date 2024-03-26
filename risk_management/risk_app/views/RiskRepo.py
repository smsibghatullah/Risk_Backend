# snippets/views.py
from rest_framework import generics
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import filters
from risk_app.models import RiskRepo
from risk_app.serializers.risk_repo import RiskRepoSerializer
from django.db.models import Q


class RiskRepoList(generics.ListCreateAPIView):
  
    queryset = RiskRepo.objects.all()
    serializer_class = RiskRepoSerializer
    def get_queryset(self):
        department_id = None
        if 'department_id' in self.kwargs:
            department_id = self.kwargs['department_id']
       
        if department_id:
            qs = RiskRepo.objects.filter()
            qs = qs.filter(department_id=self.kwargs['department_id'])
            return qs
        return super().get_queryset()

class RiskRepoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RiskRepo.objects.all()
    serializer_class = RiskRepoSerializer



class RiskRepoSearch(generics.ListAPIView):
    queryset = RiskRepo.objects.all()
    serializer_class = RiskRepoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'department_id']

    def get_queryset(self):
        queryset = self.queryset
        search_query = self.request.query_params.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(department_id__icontains=search_query)
            )
        return queryset   