from rest_framework import serializers
from risk_app.models import RiskPrioritization


class RiskPrioritizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = RiskPrioritization
        fields = '__all__'