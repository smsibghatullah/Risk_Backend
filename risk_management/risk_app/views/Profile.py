# snippets/views.py
from rest_framework import generics
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from risk_app.models import Profile
from risk_app.serializers.profile import ProfileSerializer



class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def get_queryset(self):
        """
        Optionally restricts the returned articles to given regions,
        by filtering against a `regions` query parameter in the URL.
        """
        location__query = self.request.query_params.get("location", None)
        if location__query:
            qs = Profile.objects.filter()
            # print(departments.split(self.region_separator))
            qs = qs.filter(location__contains=location__query)
            return qs
        return super().get_queryset()
   
   
    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = ProfileSerializer(queryset, many=True)
    #     user_groups = []
    #     for group in request.user.groups.values_list('name', flat=True):
    #         user_groups.append(group)
    #     if 'profile' not in user_groups:
    #         raise ValidationError('You have already signed up')
    #     return Response(serializer.data)      
     

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
