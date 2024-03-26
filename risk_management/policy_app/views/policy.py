# snippets/views.py
from rest_framework import generics
from rest_framework.response import Response

from policy_app.models.policy import Policy, RegulatoryLaws
from policy_app.models.controls import Control, IssueControl

from policy_app.serializers.policy import PolicySerializer, RegulatoryLawsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.db.models import Q


class PolicyList(generics.ListCreateAPIView):
    # permission_required = "audit_app.view_annualplan"
    # permission_classes = (IsAuthenticated,)

    queryset = Policy.objects.all()


    search_fields = [ 'name','departments', 'owner', 'state', 'date_approval', 'pilcy_edit','policy_text']
    filter_backends = (filters.SearchFilter,)


    serializer_class = PolicySerializer
    def get_queryset(self):
        name__query = self.request.query_params.get("name", None)
        if name__query:
            qs = Policy.objects.filter()
            # print(departments.split(self.region_separator))
            qs = qs.filter(name__contains=name__query)
            # qs = qs.filter(title__in=title.split(self.region_separator))
            return qs
        return super().get_queryset()

        


class PolicyDepartment(generics.ListCreateAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    def get_queryset(self):
        # department_id = self.kwargs['department_id']
        departments= None
        if 'departments' in self.kwargs:
            departments = self.kwargs['departments']
        if departments:
            qs = Policy.objects.filter()
            print(departments)
            qs = qs.filter(departments=self.kwargs['departments'])

       
          

        # owner__query = self.request.query_params.get("owner", None)
        # if owner__query:
        #     qs = Policy.objects.filter()
        #     qs = qs.filter(owner__contains=owner__query)
           
            return qs
        return super().get_queryset()

class PolicyDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)

    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    
    def update(self, request, *args, **kwargs):
        model = instance = self.get_object()
        serializer = PolicySerializer(model, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)
    
class Policysearch(generics.ListCreateAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer 

    def get_queryset(self):
        queryset = self.queryset
        search_query = self.request.query_params.get('q', None)
        if search_query is not None:
            query = Q()
            for field in Policy._meta.fields:
                if field.name == 'id':
                    continue
                lookup = f'{field.name}__icontains'
                query |= Q(**{lookup: search_query})
            queryset = queryset.filter(query)
        return queryset     

class RegulatoryLawsList(generics.ListCreateAPIView):
    # permission_required = "audit_app.view_annualplan"
    # permission_classes = (IsAuthenticated,)

    queryset = RegulatoryLaws.objects.all()
    serializer_class = RegulatoryLawsSerializer
    def get_queryset(self):
        name__query = self.request.query_params.get("name", None)
        if name__query:
            qs = RegulatoryLaws.objects.filter()
            # print(departments.split(self.region_separator))
            qs = qs.filter(name__contains=name__query)
            # qs = qs.filter(title__in=title.split(self.region_separator))
            return qs
        return super().get_queryset()  


class RegulatoryLawssearch(generics.ListCreateAPIView):
    queryset = RegulatoryLaws.objects.all()
    serializer_class = RegulatoryLawsSerializer

    def get_queryset(self):
        queryset = self.queryset
        search_query = self.request.query_params.get('q', None)
        if search_query is not None:
            query = Q()
            for field in RegulatoryLaws._meta.fields:
                if field.name == 'id':
                    continue
                lookup = f'{field.name}__icontains'
                query |= Q(**{lookup: search_query})
            queryset = queryset.filter(query)
        return queryset  



class RegulatoryLawsDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)

    queryset = RegulatoryLaws.objects.all()
    serializer_class = RegulatoryLawsSerializer
    
    def update(self, request, *args, **kwargs):
        model = self.get_object()
        serializer = RegulatoryLawsSerializer(model, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print("here")
        return Response(serializer.data)
    


class PolicyRegulatoryLawsList(generics.ListCreateAPIView):
    # permission_required = "audit_app.view_annualplan"
    # permission_classes = (IsAuthenticated,)

    queryset = RegulatoryLaws.objects.all()
    serializer_class = RegulatoryLawsSerializer
    def get_queryset(self):
        name__query = self.request.query_params.get("policyId", None)
        if name__query:
            qs = RegulatoryLaws.objects.filter()
            control_queryset = Control.objects.values('regulatory_laws').filter(policy=name__query)
            regulatory_laws_id = []
            for regulatory_laws in control_queryset:
                regulatory_laws_id.append(regulatory_laws['regulatory_laws'])
            qs = qs.filter(pk__in=regulatory_laws_id)
            return qs
        return super().get_queryset()
