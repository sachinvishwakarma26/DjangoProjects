from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        data=JSONParser().parse(stream)
        id=data.get('id',None)
        if id is not None:
            emp=Employee.objects.get(id=id)
            serializer=EmployeeSerializer(emp)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        qs=Employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        data=JSONParser().parse(stream)
        serializer=EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Resource Created Succesfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        data=JSONParser().parse(stream)
        id=data.get('id')
        emp=Employee.objects.get(id=id)
        serializer=EmployeeSerializer(emp,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Resource Updated Succesfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
