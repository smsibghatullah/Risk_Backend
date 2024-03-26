# snippets/views.py
from rest_framework import generics
from rest_framework.response import Response
from audit_app.models.annual_plan import AnnualPlan, AuditEngagement, AuditEngagementAttachment, AuditProgramRepo, AuditProgram,AuditProgramAttachment
from audit_app.serializers.annual_plan import AnnualPlanSerializer, AuditEngagementSerializer,\
    AuditEngagementAttachmentSerializer, AuditProgramRepoSerializer, AuditProgramSerializer,AuditProgramAttachmentSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.db.models import Q
from rest_framework.parsers import MultiPartParser





class AnnualPlanList(generics.ListCreateAPIView):
    # permission_required = "audit_app.view_annualplan"
    # permission_classes = (IsAuthenticated,)
    search_fields = ['title', 'departments']
    filter_backends = (filters.SearchFilter,)
    queryset = AnnualPlan.objects.all()
    serializer_class = AnnualPlanSerializer
    # def get_queryset(self):
    #     title__query = self.request.query_params.get("title", None)
    #     if title__query:
    #         qs = AnnualPlan.objects.filter()
    #         # print(departments.split(self.region_separator))
    #         qs = qs.filter(title__contains=title__query)
    #         # qs = qs.filter(title__in=title.split(self.region_separator))
    #         return qs
    #     return super().get_queryset()

class AnnualPlanDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = AnnualPlan.objects.all()
    serializer_class = AnnualPlanSerializer

class AnnualPlansearch( generics.ListCreateAPIView):
    queryset = AnnualPlan.objects.all()
    serializer_class = AnnualPlanSerializer

    def get_queryset(self):
        queryset = self.queryset
        search_query = self.request.query_params.get('q', None)
        if search_query is not None:
            query = Q()
            for field in AnnualPlan._meta.fields:
                if field.name == 'id':
                    continue
                lookup = f'{field.name}__icontains'
                query |= Q(**{lookup: search_query})
            queryset = queryset.filter(query)
        return queryset 


class AuditEngagementList(generics.ListCreateAPIView):
    queryset = AuditEngagement.objects.all()
    serializer_class = AuditEngagementSerializer

    

    def get_queryset(self):
       name__query = self.request.query_params.get("name", None)
       if name__query:
            qs = AuditEngagement.objects.filter()
            # print(departments.split(self.region_separator))
            qs = qs.filter(name__contains=name__query)
            # qs = qs.filter(title__in=title.split(self.region_separator))
            return qs
       return super().get_queryset()


class AuditEngagementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuditEngagement.objects.all()
    serializer_class = AuditEngagementSerializer
    def update(self, request, *args, **kwargs):
        model = self.get_object()
        serializer = AuditEngagementSerializer(model, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)
    
class AuditEngagementsearch( generics.ListCreateAPIView):
    queryset = AuditEngagement.objects.all()
    serializer_class = AuditEngagementSerializer

    def get_queryset(self):
        queryset = self.queryset
        search_query = self.request.query_params.get('q', None)
        if search_query is not None:
            query = Q()
            for field in AuditEngagement._meta.fields:
                if field.description == 'id':
                    continue
                lookup = f'{field.description}__icontains'
                query |= Q(**{lookup: search_query})
            queryset = queryset.filter(query)
        return queryset    

class AuditEngagementAttachmentList(generics.ListCreateAPIView):
    queryset = AuditEngagementAttachment.objects.all()
    serializer_class = AuditEngagementAttachmentSerializer

     
class AuditProgramAttachmentList(generics.ListCreateAPIView):
    queryset = AuditProgramAttachment.objects.all()
    serializer_class = AuditProgramAttachmentSerializer

class AuditEngagementAttachmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuditEngagementAttachment.objects.all()
    serializer_class = AuditEngagementAttachmentSerializer


class AuditProgramRepoList(generics.ListCreateAPIView):
    queryset = AuditProgramRepo.objects.all()
    serializer_class = AuditProgramRepoSerializer


class AuditProgramRepoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuditProgramRepo.objects.all()
    serializer_class = AuditProgramRepoSerializer



class AuditProgramRepoSearch(generics.ListAPIView):
    queryset = AuditProgramRepo.objects.all()
    serializer_class = AuditProgramRepoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'summary', 'description', 'category']

    def get_queryset(self):
        queryset = self.queryset
        search_query = self.request.query_params.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(summary__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(category__icontains=search_query)
            )
        return queryset



class AuditProgramList(generics.ListCreateAPIView):
    queryset = AuditProgram.objects.all()
    serializer_class = AuditProgramSerializer


class AuditProgramDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuditProgram.objects.all()
    serializer_class = AuditProgramSerializer
     


class AuditProgramSearch(generics.ListAPIView):
    queryset = AuditProgram.objects.all()
    serializer_class = AuditProgramSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category', 'description', 'title_of_procedure', 'summary_of_procedure']

    def get_queryset(self):
        queryset = self.queryset
        search_query = self.request.query_params.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(category__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(title_of_procedure__icontains=search_query) |
                Q(summary_of_procedure__icontains=search_query)
            )
        return queryset



