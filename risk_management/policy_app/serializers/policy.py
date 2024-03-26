from rest_framework import serializers
from policy_app.models.policy import Policy, RegulatoryLaws


class PolicySerializer(serializers.ModelSerializer):

    class Meta:
        model = Policy
        fields = '__all__'
    def validate(self, data):
        # other wise you can set default value of age here,
        if data.get('state',None) == None:  # this conditon will be true only when age = serializer.IntergerField(required=False)
            data['state'] = 'Draft'
        return data


class RegulatoryLawsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegulatoryLaws
        fields = '__all__'
    def validate(self, data):
        # other wise you can set default value of age here,
        # if data.get('state',None) == None:  # this conditon will be true only when age = serializer.IntergerField(required=False)
        #     data['state'] = 'Draft'
        return data
