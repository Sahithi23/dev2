############## DJANGO GENERAL IMPORT #############
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import views
from django.shortcuts import render
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate
from django.db.models import Q
from django.core.files.storage import default_storage as storage
from django.db import IntegrityError

############## PYTHON GENERAL IMPORT #############
import json
import os

##############  APP SPECIFIC IMPORT  #############
from .serializers import MyTokenObtainPairSerializer, MyTokenRefreshSerializer
from .models import User # , SITE_MAPPING, SITEID, ROLES


@csrf_exempt
def signup_view(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
    except:
        data = request.POST
    context = {"flag": "error", "status": 400}

    try:
        if data['username'] == '':
            context['message'] = 'Please enter username'
        elif data['password'] == '':
            context['message'] = 'Please enter password'
        elif data['first_name'] == '':
            context['message'] = 'Please enter first name'
        elif data['last_name'] == '':
            context['message'] = 'Please enter last name'
        elif data['site_id'] == '':
            context['message'] = 'Please enter site ID'
        elif data['role'] == '':
            context['message'] = 'Please select role'

        if 'message' in context:
            return HttpResponse(json.dumps(context), status=400, content_type='application/json')

        user = User.objects.create(username=data['username'], first_name=data['first_name'],
                                   last_name=data['last_name'], email=data['email'], mobile=data['mobile'],
                                   site_id=str(data['site_id']))
        user.set_password(data['password'])
        user.is_active = False
        user.user_role = str(data['role'])
        # try:
        assign_role(user, ROLE_MAPPING.get(user.user_role))
        # except:
        #     pass
        user.save()
        context = {"flag": "success", "message": "Signup Success", "status": 200}

    except IntegrityError:
        context['message'] = "Username already Exists"
        return HttpResponse(json.dumps(context), status=400, content_type='application/json')
    except Exception as e:
        context['message'] = str(e)
        return HttpResponse(json.dumps(context), status=400, content_type='application/json')

    return HttpResponse(json.dumps(context), status=200, content_type='application/json')


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer


class LoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        context = {'flag': 'error', 'status': 400}

        username = request.data.get('username', None)
        password = request.data.get('password', None)
        # site_id = request.data.get('site_id', None)
        # print('username--------', username)
        # print('password-----', '***')
        # print('site_id-----', site_id)
        if not username:
            context['message'] = 'Please enter username'
        elif not password:
            context['message'] = 'Please enter password'
        # elif not site_id:
        #     context['message'] = 'Please provide site ID'

        if 'message' in context:
            return HttpResponse(json.dumps(context), status=400, content_type='application/json')

        try:
            usr = User.objects.get(username=username)
            if not usr.is_active:
                context['message'] = "User Account is Deactivated, Please Contact Admin to Get Access"
                return HttpResponse(json.dumps(context), status=400, content_type='application/json')
            user = authenticate(username=username, password=password)
            # if not user:
            #     context['message'] = "Invalid credentials"
            #     return HttpResponse(json.dumps(context), status=400, content_type='application/json')
            # elif not user.site_id == str(site_id):
            #     context['message'] = "Invalid site ID"
            #     return HttpResponse(json.dumps(context), status=400, content_type='application/json')
        except User.DoesNotExist:
            context['message'] = "Invalid username or password"
            return HttpResponse(json.dumps(context), status=400, content_type='application/json')

        obtserializer = MyTokenObtainPairSerializer
        token = obtserializer.get_token(user)

        context = {'flag': 'success', 'status': 200, 'message': 'login success', "username": username,
                   "refresh_token": str(token), "access_token": str(token.access_token)}
        if user.is_reset_user:
            context['message'] = 'change password'

        try:
            profile_photo = user.profile_pic.url
        except:
            profile_photo = None
        context['profile_pic'] = str(profile_photo)

        roles = get_user_roles_list(user.site_id)
        role = ""
        for obj in roles:
            if obj['id'] == user.user_role:
                role = obj['name']
                break
        context['role'] = role

        return HttpResponse(json.dumps(context), status=200, content_type='application/json')


class AccessRefreshView(views.APIView):
    def post(self, request, *args, **kwargs):
        context = {'flag': 'success'}
        refresh = request.data.get('refresh', None)
        if refresh == '':
            context['flag'] = 'error'
            context['message'] = 'Please enter refresh token'

        if len(refresh) > 1:
            refserializer = MyTokenRefreshSerializer
            attrs = {'refresh': refresh}
            try:
                token = refserializer.validate(attrs)
                if token['access'] is not None:
                    return HttpResponse(
                        json.dumps({"access_token": str(token['access']), "flag": "success",
                                    "message": "success", "status": 200}),
                        status=200,
                        content_type="application/json"
                    )
                else:
                    return HttpResponse(
                        json.dumps({'message': "Token is invalid or expired", "flag": "error", "status": 400}),
                        status=400,
                        content_type="application/json"
                    )
            except TokenError:
                return HttpResponse(
                    json.dumps({'message': 'Token is invalid or expired', "flag": "error", "status": 400}),
                    status=400,
                    content_type="application/json"
                )
