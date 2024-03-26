# snippets/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from master_app.models.company_setup import CompanySetup
from master_app.serializers.companysetup import CompanySetupSerializer


class CompanySetupList(generics.ListCreateAPIView):
    queryset = CompanySetup.objects.all()
    serializer_class = CompanySetupSerializer
    def get_queryset(self):
     name_query = self.request.query_params.get("name", None)
     if name_query:
         qs = CompanySetup.objects.filter()
         # print(departments.split(self.region_separator))
         qs = qs.filter(name__contains=name_query)
         return qs
     return super().get_queryset()

    # def post(self, request, *args, **kwargs):
    #     print(request)
    #     print(args)
    #     print(kwargs)
    #     return self.create(request, *args, **kwargs)

    
class CompanySetupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanySetup.objects.all()
    serializer_class = CompanySetupSerializer
