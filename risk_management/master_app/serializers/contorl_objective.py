from rest_framework import serializers
from master_app.models.control_objective import ControlObjective


class ControlObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlObjective
        fields = '__all__'
