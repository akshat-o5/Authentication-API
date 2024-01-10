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


    # Validaing password and confirm password for similarity
    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError("Paswword and Confirm Password are not same")
        return data

    def create(self, validate_data):
        return Human.objects.create_user(**validate_data)    







class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = '__all__'      




class HumanLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)
    class Meta:
        model = Human
        fields = ['email', 'password']        





class HumanProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = ['id', 'name', 'email']
                    


class ChangePasswordSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=100, style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(max_length=100, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', 'password2']

  def validate(self, data):
    password = data.get('password')
    password2 = data.get('password2')
    human = self.context.get('human')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password donot match")
    human.set_password(password)
    human.save()
    return data