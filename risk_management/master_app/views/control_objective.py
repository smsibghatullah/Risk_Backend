from rest_framework import generics
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from master_app.models.control_objective import ControlObjective
from master_app.models.department import DocComment
from master_app.serializers.contorl_objective import ControlObjectiveSerializer
from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView



from master_app.serializers.department import CommentSerializer


class ControlObjectiveList( generics.ListCreateAPIView):
    queryset = ControlObjective.objects.all()
    serializer_class = ControlObjectiveSerializer

    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = ControlObjectiveSerializer(queryset, many=True)
    #     user_groups = []
    #     for group in request.user.groups.values_list('description', flat=True):
    #         user_groups.append(group)
    #     return Response(serializer.data)
    #
    def get_queryset(self):
        title__query = self.request.query_params.get("description", None)
        if title__query:
            qs = ControlObjective.objects.filter()
            # print(departments.split(self.region_separator))
            qs = qs.filter(description__contains=title__query)
            # qs = qs.filter(title__in=title.split(self.region_separator))
            return qs
        return super().get_queryset()

class ControlObjectiveSeach( generics.ListCreateAPIView):
    queryset = ControlObjective.objects.all()
    serializer_class = ControlObjectiveSerializer

    def get_queryset(self):
        queryset = self.queryset
        search_query = self.request.query_params.get('q', None)
        if search_query is not None:
            query = Q()
            for field in ControlObjective._meta.fields:
                if field.name == 'id':
                    continue
                lookup = f'{field.name}__icontains'
                query |= Q(**{lookup: search_query})
            queryset = queryset.filter(query)
        return queryset        

class ControlObjectiveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ControlObjective.objects.all()
    serializer_class = ControlObjectiveSerializer


class TodoListApiView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the item items for given requested user
        '''
        docId = self.request.query_params.get("docId", None)
        belogTo = self.request.query_params.get("belogTo", None)
        items = DocComment.objects.all()
        if docId is not None and belogTo is not None:
            items = DocComment.objects.filter(docId = docId, belogTo=belogTo)
        serializer = CommentSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the item with given item data
        '''
        data = {
            'belogTo': request.data.get('belogTo'), 
            'docId': request.data.get('docId'), 
            'comment': request.data.get('comment'), 
        }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)