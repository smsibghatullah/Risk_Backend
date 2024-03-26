# snippets/views.py
from rest_framework import generics
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import filters
from risk_app.models import RiskMatrix
from risk_app.serializers.risk_matrix import RiskMatrixSerializer



class RiskMatrixList(generics.ListCreateAPIView):
    search_fields = ['combine']
    ordering_fields = ['id','likehood', 'impact', 'combine', 'score', 'likehood_rate', 'impact_rate', 'score_rate']
    filter_backends = (filters.SearchFilter,)
    queryset = RiskMatrix.objects.all()
    serializer_class = RiskMatrixSerializer
    def get_queryset(self):
        """
        Optionally restricts the returned articles to given regions,
        by filtering against a `regions` query parameter in the URL.
        """
        likehood_query = self.request.query_params.get("likehood", None)
        if likehood_query:
            qs = RiskMatrix.objects.filter()
            # print(departments.split(self.region_separator))
            qs = qs.filter(likehood__contains=likehood_query)
            return qs
        return super().get_queryset()
   
    def list(self, request):
        queryset = self.get_queryset()
        serializer =  RiskMatrixSerializer(queryset, many=True)
        user_groups = []
        for group in request.user.groups.values_list('name', flat=True):
            user_groups.append(group)
        if 'risk_matrix' not in user_groups:
            raise ValidationError('You have already signed up')
        return Response(serializer.data)      


class RiskMatrixDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RiskMatrix.objects.all()
    serializer_class = RiskMatrixSerializer
