from rest_framework import serializers
from risk_app.models import RiskRepo
from master_app.serializers.department import DepartmentSerializer

class RiskRepoSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(read_only=True)
    class Meta:
        model = RiskRepo
        fields = '__all__'
