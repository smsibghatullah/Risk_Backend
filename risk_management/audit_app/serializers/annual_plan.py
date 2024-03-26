from rest_framework import serializers
from audit_app.models.annual_plan import AnnualPlan, AuditEngagement,\
    AuditEngagementAttachment, AuditProgramRepo, AuditProgram,AuditProgramAttachment


class AnnualPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualPlan
        fields = '__all__'

    # def validate(self, data):
    #     if data.get('state',None) == None:  # this conditon will be true only when age = serializer.IntergerField(required=False)
    #         data['state'] = 'draft'
    #     return data


class AuditEngagementSerializer(serializers.ModelSerializer):
    # department = serializers.SlugRelatedField( slug_field='name', read_only=True)
    
    class Meta:
        model = AuditEngagement
        fields = '__all__'


class AuditEngagementAttachmentSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)
    class Meta:
        model = AuditProgramRepo
        fields = '__all__'


class AuditProgramRepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditProgramRepo
        fields = '__all__'


class AuditProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditProgram
        fields = '__all__'

class AuditProgramAttachmentSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)
    class Meta:
        model = AuditProgramAttachment
        fields = '__all__'