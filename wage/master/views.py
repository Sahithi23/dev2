from django.shortcuts import render
from .models import Doctor_Master
from datetime import date,datetime, timedelta
import json
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.conf import settings
from .serializers import DoctorSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView
from django.http import HttpResponse, JsonResponse, response
from django.shortcuts import render_to_response
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.core.serializers.json import DjangoJSONEncoder

def doctor_list(request, bp_type='BP1'):
    # Combined data of the Patients and Appointments
    # bp_type = create_recommendations_call(request)
    cursor = connections[bp_type].cursor()
    try:
        cursor.execute("SELECT USERID, USERSTATUS, SURNAME ,FIRSTNAME FROM USERS")
    except QueryDoesNotExist:
        pass
    data = cursor.fetchall()
        # print(data)
    ldata = []
    content = {}
    for q in data:
        content = {"userid":q[0],"userstatus":q[1],"surname":q[2],"firstname":q[3]}
        ldata.append(content)
        
    for i in ldata:
        Doctor_Master.objects.create(UID=list(i.values())[0],firstname=list(i.values())[3],
        lastname=list(i.values())[2],doctor_status=list(i.values())[1])

    return HttpResponse(json.dumps({"message" : "success"}), content_type="application/json")

class DoctorListView(ListAPIView):
    queryset = Doctor_Master.objects.all()
    serializer_class = DoctorSerializer

# def appointment_call(request):
#     try:
#         appointment_list(request, bp_type='BP1', site_id=settings.PRACTICE_A_SITEID)
#     except Exception as e:
#         print(e)
#     try:
#         appointment_list(request, bp_type='BP2', site_id=settings.PRACTICE_B_SITEID)
#     except Exception as e:
#         print(e)