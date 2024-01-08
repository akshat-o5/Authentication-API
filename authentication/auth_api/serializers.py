from rest_framework import serializers
from auth_api.models import Human


class HumanRegisterationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model=Human
        fields=['email', 'name', 'tnc', 'password', 'password2']
        extra_kwargs={
            'password':{'write_only':True}
        }