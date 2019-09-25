from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from django.views.generic import View
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        print('before parsing')
        data=JSONParser().parse(stream)
        print('after')
        id=data.get('id',None)
        print('id')
        if id is not None:
            emp=Employee.objects.get(id=id)
            eserializer=EmployeeSerializer(emp)
            json_data=JSONRenderer().render(eserializer.data)
        else:
            qs= Employee.objects.all()
            eserializer=EmployeeSerializer(qs,many=True)
            json_data = JSONRenderer().render(eserializer.data)
        return HttpResponse(json_data,content_type='application/json')
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        data=JSONParser().parse(stream)
        eserializer=EmployeeSerializer(data=data)
        print(eserializer.is_valid())
        eserializer.save()
        msg={'msg':'Resource created successfully'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type='application/json')
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        data=JSONParser().parse(stream)
        emp=Employee.objects.get(id=data.get('id'))
        # eserializer=EmployeeSerializer(emp,data=data)
        eserializer=EmployeeSerializer(emp,data=data,partial=True)
        if eserializer.is_valid():
            eserializer.save()
            msg={'msg':'Resource updated successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(eserializer.errors)
        return HttpResponse(json_data,content_type='application/json')
