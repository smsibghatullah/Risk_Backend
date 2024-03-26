from rest_framework import serializers
from master_app.models.department import Department, DocComment, SubDepartment


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class SubDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDepartment
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocComment
        fields = '__all__'

