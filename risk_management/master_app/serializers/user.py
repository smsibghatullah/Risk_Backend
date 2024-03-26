from rest_framework import serializers

from django.contrib.auth.models import User
from master_app.serializers.group import GroupSerializer, PermissionSerializer


class UserSerializer(serializers.ModelSerializer):
    user_permissions = PermissionSerializer(many=True, read_only=True)
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username','is_superuser', 'user_permissions', 'first_name' ,'last_name', 'email', 'groups', 'department', 'usertype']
        extra_kwargs = {'password': {'write_only': False}}

    def update(self, instance, validated_data, **kwargs):
        # groups_data = validated_data.pop('groups')

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.usertype = validated_data.get('usertype', instance.usertype)
        instance.save()


        # instance.groups.clear()
        # print(groups_data)
        # for group_data in groups_data:
        #     instance.groups.add(group_data)
        return instance
   
# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        groups_data = validated_data.pop('groups')
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        for group_data in groups_data:
            user.groups.add(group_data)

        return user