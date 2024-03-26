from rest_framework import serializers
from master_app.models.company_setup import CompanySetup
from master_app.serializers.department import DepartmentSerializer

class CompanySetupSerializer(serializers.ModelSerializer):
#     departments = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)

    class Meta:
        model = CompanySetup
        fields = '__all__'

