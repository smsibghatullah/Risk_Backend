from rest_framework import serializers
from policy_app.models.controls import Control,IssueControl


class ControlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Control
        fields = '__all__'


class IssueControlSerializer(serializers.ModelSerializer):

    class Meta:
        model = IssueControl
        fields = '__all__'
