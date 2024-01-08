from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from auth_api.serializers import HumanRegisterationSerializer

# Create your views here.

class HumanRegisterationView(APIView):
    def post(self, request, format=None):
        serializer = HumanRegisterationSerializer(data=request.data)
        return Response({'msg':'Registeration Successful'})