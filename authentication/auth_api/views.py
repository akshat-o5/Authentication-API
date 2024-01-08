from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from auth_api.serializers import HumanRegisterationSerializer, HumanSerializer, HumanLoginSerializer
from auth_api.models import Human, HumanManager
from django.contrib.auth import authenticate
from auth_api.renderers import HumanRenderer

# Create your views here.

class HumanRegisterationView(APIView):

    renderer_classes = [HumanRenderer]

    def get(self, request, format=None):
        humans = Human.objects.all()
        serializer = HumanSerializer(humans, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HumanRegisterationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Registeration Successful'},status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    









class HumanLoginView(APIView):

    renderer_classes = [HumanRenderer]

    def post(self, request, forat=None):
        serializer = HumanLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            human = authenticate(email=email, password=password)
            if human is not None:
                return Response({'msg':'Login Successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)      
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         