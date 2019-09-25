from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json

# Create your views here.
def employee_data_view(request):
    employee_data={'eno':100,'ename':'Sunny Leone','esal':1000,'eaddr':'Hyderabad'}
    resp='<h1>Employee No:{}<br>Employee Name:{}<br>Employee Salary:{}<br>Employee Address:{}</h1>'.format(employee_data['eno'],employee_data['ename'],employee_data['esal'],employee_data['eaddr'])
    return HttpResponse(resp)

def employee_data_jsonview(request):
    employee_data={'eno':100,'ename':'Sunny Leone','esal':1000,'eaddr':'Hyderabad'}
    json_data=json.dumps(employee_data)
    return HttpResponse(json_data,content_type='application/json')

def employee_data_jsondirectview(request):
    employee_data={'eno':100,'ename':'Sunny Leone','esal':1000000,'eaddr':'Hyderabad'}
    return JsonResponse(employee_data)

from django.views.generic import View
class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        employee_data={'eno':100,'ename':'Sunny Leone','esal':1000,'eaddr':'Hyderabad'}
        return JsonResponse(employee_data)

from testapp.mixins import JsonResponseMixin
class JsonCBV2(JsonResponseMixin,View):
    def get(self,request,*args,**kwargs):
        employee_data={'eno':100,'ename':'Sunny Leone','esal':1000,'eaddr':'Hyderabad'}
        return self.render_to_json_response(employee_data)
