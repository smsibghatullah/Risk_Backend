from rest_framework import serializers
from risk_app.models import RiskAssessment

class RiskAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskAssessment
        fields = '__all__'
