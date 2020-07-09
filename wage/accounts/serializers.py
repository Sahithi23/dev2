############## DJANGO GENERAL IMPORT #############
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework import serializers

############## PYTHON GENERAL IMPORT #############

##############  APP SPECIFIC IMPORT  #############
from .models import User  # , ROLE_MAPPING


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    @classmethod
    def validate(cls, attrs):
        data = super().validate(attrs)
        return data