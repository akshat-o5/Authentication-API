from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from auth_api.serializers import HumanRegisterationSerializer, HumanSerializer
from auth_api.models import Human, HumanManager

# Create your views here.

class HumanRegisterationView(APIView):

    def get(self, request, format=None):
        humans = Human.objects.all()
        serializer = HumanSerializer(humans, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HumanRegisterationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Registeration Successful'},status=status.HTTP_201_CREATED)
            
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    









class HumanLoginView(APIView):
    def post(self, request, forat=None):
        return Response({'msg':'Login Successful'}, status=status.HTTP_200_OK)           