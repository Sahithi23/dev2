from django.http import JsonResponse
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Doctor_Master


# @classmethod
class DoctorSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Doctor_Master
        fields = ('UID', 'firstname', 'lastname', 'doctor_status')