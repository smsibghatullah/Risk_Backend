# snippets/views.py
from rest_framework import generics
from rest_framework import filters
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from risk_app.models import ControlRatingMatrix
from risk_app.serializers.control_rating_matrix import ControlRatingMatrixSerializer



class ControlRatingMatrixList(generics.ListCreateAPIView):
    search_fields = ['=formula']
    filter_backends = (filters.SearchFilter,)
    queryset = ControlRatingMatrix.objects.all()
    serializer_class = ControlRatingMatrixSerializer
    def get_queryset(self):
            design_query= self.request.query_params.get("design", None)
            if design_query:
                qs = ControlRatingMatrix.objects.filter()
                # print(departments.split(self.region_separator))
                qs = qs.filter(design__contains=design_query)
                return qs

            return super().get_queryset()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ControlRatingMatrixSerializer(queryset, many=True)
        user_groups = []
        for group in request.user.groups.values_list('name', flat=True):
            user_groups.append(group)
        if 'control_rating_matrix' not in user_groups:
            raise ValidationError('You have already signed up')
        return Response(serializer.data)        


class ControlRatingMatrixDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ControlRatingMatrix.objects.all()
    serializer_class = ControlRatingMatrixSerializer
