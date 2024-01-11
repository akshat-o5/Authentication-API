from django.core.exceptions import ValidationError
from rest_framework import serializers
from auth_api.models import Human
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from auth_api.utils import Util


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









class SendPasswordResetEmailSerializer(serializers.Serializer):
  email = serializers.EmailField(max_length=100)
  class Meta:
    fields = ['email']

  def validate(self, data):
    email = data.get('email')
    if Human.objects.filter(email=email).exists():
      human = Human.objects.get(email = email)
      uid = urlsafe_base64_encode(force_bytes(human.id))
      print('Encoded UID', uid)
      token = PasswordResetTokenGenerator().make_token(human)
      print('Password Reset Token', token)
      link = 'http://localhost:3000/reset/'+uid+'/'+token
      print('Password Reset Link', link)
      # Send EMail
      body = 'Click Following Link to Reset Your Password '+link
      _data = {
        'subject':'Reset Your Password',
        'body':body,
        'to_email':human.email
      }
      Util.send_email(_data)
      return data
    else:
      raise serializers.ValidationError('You are not a Registered User')    










class PasswordResetSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', 'password2']

  def validate(self, data):
    try:
      password = data.get('password')
      password2 = data.get('password2')
      uid = self.context.get('uid')
      token = self.context.get('token')
      if password != password2:
        raise serializers.ValidationError("Password and Confirm Password doesn't match")
      id = smart_str(urlsafe_base64_decode(uid))
      human = Human.objects.get(id=id)
      if not PasswordResetTokenGenerator().check_token(human, token):
        raise serializers.ValidationError('Token is not Valid or Expired')
      human.set_password(password)
      human.save()
      return data
    except DjangoUnicodeDecodeError as identifier:
      PasswordResetTokenGenerator().check_token(human, token)
      raise serializers.ValidationError('Token is not Valid or Expired')      