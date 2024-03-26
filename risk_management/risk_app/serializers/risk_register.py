from rest_framework import serializers
from risk_app.models import RiskRegister


class RiskRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = RiskRegister
        fields = ('id','department_id', 'sub_department', 'status', 'title', 'root_cause', 'consequence', 'category', 
        'function_owner', 'risk_owner', 'risk_champion', 'inherent_risk_rating_likehood', 
        'inherent_risk_rating_impact', 'inherent_risk_rating_rating', 'control_description', 
        'control_design_assessement', 'control_effectiveness_assessement', 'overall_control_rating',
        'residual_risk_scoring_score', 'risk_responses', 'treatment_required', 'action_plan', 'action_plan_owner',
         'implementation_date', 'parent_id', 'updated_at', 'assessment_date', 
         'next_review_date', 'previous_assessment','file_name','file', 'review_status')


 
