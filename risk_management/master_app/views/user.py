from rest_framework import  generics
from rest_framework.response import Response
from rest_framework.views import APIView
# from  knox.models  import AuthToken
from django.contrib.auth.models import User
from master_app.serializers.user import UserSerializer, RegisterSerializer
from rest_framework import filters
from django.db.models import Q

#  Register  API

class UserList(generics.ListCreateAPIView):
    search_fields = [ 'first_name','last_name','email', 'username', 'usertype']
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    filter_backends = (filters.SearchFilter,)
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def put(self, request, *args, **kwargs):
        # return self.updatereturnall(request, *args, **kwargs)
        return {"Taha":"user"}

class UpdateUser(APIView):
   
    def patch(self, request, *args, **kwargs):
        _user = User.objects.get(id=request.data['id'])
        _user.first_name = request.data['first_name']
        _user.last_name = request.data['last_name']
        _user.department = request.data['department']
        _user.usertype = request.data['usertype']
        _user.groups.clear()
        _user.save()
        if len(request.data['password']) > 0:
            _user.set_password(request.data['password'])
        _user.save()
        groups_data = request.data['groups']
        for group_data in groups_data:
            _user.groups.add(group_data)

        return Response(status=200)
class RegisterAPI(generics.GenericAPIView):
        # queryset = User.objects.all()
        serializer_class = RegisterSerializer

        def post(self, request, *args, **kwargs):
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.save()
                return Response({
                "user":  UserSerializer(user,  context=self.get_serializer_context()).data,
                # "token":  AuthToken.objects.create(user)[1]
                })
        
class Usersearch(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = self.queryset
        search_query = self.request.query_params.get('q', None)
        if search_query is not None:
            query = Q()
            for field in User._meta.fields:
                if field.name == 'id':
                    continue
                lookup = f'{field.name}__icontains'
                query |= Q(**{lookup: search_query})
            queryset = queryset.filter(query)
        return queryset         