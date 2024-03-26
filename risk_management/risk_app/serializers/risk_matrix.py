from rest_framework import serializers
from risk_app.models import RiskMatrix


class RiskMatrixSerializer(serializers.ModelSerializer):

    class Meta:
        model = RiskMatrix
        fields = '__all__'

        
