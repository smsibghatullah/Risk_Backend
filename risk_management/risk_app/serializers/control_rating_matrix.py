from rest_framework import serializers
from risk_app.models import ControlRatingMatrix


class ControlRatingMatrixSerializer(serializers.ModelSerializer):

    class Meta:
        model = ControlRatingMatrix
        fields = '__all__'


       
        