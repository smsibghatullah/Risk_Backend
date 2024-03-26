# snippets/views.py
from rest_framework import generics
from policy_app.models.controls import Control, IssueControl
from policy_app.serializers.control import ControlSerializer, IssueControlSerializer
from master_app.models.control_objective import ControlObjective
from master_app.serializers.contorl_objective import ControlObjectiveSerializer
from rest_framework.permissions import IsAuthenticated
from master_app.models.control_objective import ControlObjective
from master_app.serializers.contorl_objective import ControlObjectiveSerializer
from django.db.models import Q

#
# class PolicyControlObjectiveList(generics.ListCreateAPIView):
#     # permission_required = "audit_app.view_annualplan"
#     # permission_classes = (IsAuthenticated,)
#
#     queryset = ControlObjective.objects.all()
#     serializer_class = ControlObjectiveSerializer
#     control_queryset = Control.objects.all()
#     print(control_queryset)
#     print("control_queryset")
#     def get_queryset(self):
#         name__query = self.request.query_params.get("policyId", None)
#         if name__query:
#             qs = ControlObjective.objects.filter()
#             # print(departments.split(self.region_separator))
#             qs = qs.filter(policy=name__query)
#             # qs = qs.filter(title__in=title.split(self.region_separator))
#             return qs
#         return super().get_queryset()



class ControlList(generics.ListCreateAPIView):
    # permission_required = "audit_app.view_annualplan"
    # permission_classes = (IsAuthenticated,)

    queryset = Control.objects.all()
    serializer_class = ControlSerializer
    def get_queryset(self):
        description__query = self.request.query_params.get("description", None)
        if description__query:
            qs = Control.objects.filter()
            # print(departments.split(self.region_separator))
            qs = qs.filter(description__contains=description__query)
            # qs = qs.filter(title__in=title.split(self.region_separator))
            return qs
        return super().get_queryset()



class ControlDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Control.objects.all()
    serializer_class = ControlSerializer


class IssueControlList(generics.ListCreateAPIView):
    # permission_required = "audit_app.view_annualplan"
    # permission_classes = (IsAuthenticated,)

    queryset = IssueControl.objects.all()
    serializer_class = IssueControlSerializer
    def get_queryset(self):
            issue_reference_number__query = self.request.query_params.get("issue_reference_number", None)
            if issue_reference_number__query:
                qs = IssueControl.objects.filter()
                # print(departments.split(self.region_separator))
                qs = qs.filter(issue_reference_number__contains=issue_reference_number__query)
                # qs = qs.filter(title__in=title.split(self.region_separator))
                return qs
            else:
                qs = IssueControl.objects.filter()
                return qs




class IssueControlDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = IssueControl.objects.all()
    serializer_class = IssueControlSerializer


class PolicyControlObjectiveList(generics.ListCreateAPIView):
    # permission_required = "audit_app.view_annualplan"
    # permission_classes = (IsAuthenticated,)

    queryset = ControlObjective.objects.all()
    serializer_class = ControlObjectiveSerializer

    def get_queryset(self):
        name__query = self.request.query_params.get("policyId", None)
        if name__query:
            qs = ControlObjective.objects.filter()
            control_queryset = Control.objects.values('control_objective').filter(policy=name__query)
            control_objective_id = []
            for control_objective in control_queryset:
                control_objective_id.append(control_objective['control_objective'])
            qs = qs.filter(pk__in=control_objective_id)
            # qs = qs.filter(id=control_queryset['control_objective'])
            return qs
        return super().get_queryset()

class Controlsearch(generics.ListCreateAPIView):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer  

    def get_queryset(self):
        queryset = self.queryset
        search_query = self.request.query_params.get('q', None)
        if search_query is not None:
            query = Q()
            for field in Control._meta.fields:
                if field.name == 'id':
                    continue
                lookup = f'{field.name}__icontains'
                query |= Q(**{lookup: search_query})
            queryset = queryset.filter(query)
        return queryset   