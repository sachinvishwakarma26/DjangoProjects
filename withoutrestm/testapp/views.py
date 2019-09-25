from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
import json
from django.http import HttpResponse
from django.core.serializers import serialize
from testapp.mixins import SerializeMixin,HttpResponseMixin
from testapp.utils import is_validjson
from testapp.forms import EmployeeForm
# class EmployeeCRUDCBV(SerializeMixin,HttpResponseMixin,View):
#     def get_object_by_id(self,id=None):
#         try:
#             obj=Employee.objects.get(id=id)
#         except Employee.DoesNotExist:
#             obj=None
#         return obj
#
#     def get(self,request,id,*args,**kwargs):
#         print('inside get method')
#         try:
#             emp=Employee.objects.get(id=id)
#             json_data=self.serialize([emp,])
#             return self.render_to_http_response(json_data)
#         except Employee.DoesNotExist:
#             json_data=json.dumps({'msg':'The required record not available'})
#             return self.render_to_http_response(json_data,status=404)
#     def put(self,request,id,*args,**kwargs):
#         obj=self.get_object_by_id(id)
#         if obj is None:
#             json_data=json.dumps({'msg':'No matched record found to update'})
#             return self.render_to_http_response(json_data,status=404)
#         valid_json= is_validjson(request.body)
#         if not valid_json:
#             error_msg=json.dumps({'msg':'please valid json only'})
#             return self.render_to_http_response(error_msg,status=400)
#         data=json.loads(request.body)
#         current_emp={
#         'eno':obj.eno,
#         'ename':obj.ename,
#         'esal':obj.esal,
#         'eaddr':obj.eaddr,
#         }
#         for key,value in data.items():
#             current_emp[key]=value
#         form=EmployeeForm(current_emp,instance=obj)
#         if form.is_valid():
#             obj=form.save(commit=True)
#             json_data=self.serialize([obj,])
#             return self.render_to_http_response(json_data,status=201)
#         if form.errors:
#             json_data=json.dumps(form.errors)
#             return self.render_to_http_response(json_data,status=400)
#     def delete(self,request,id,*args,**kwargs):
#         obj=self.get_object_by_id(id)
#         if obj is None:
#             json_data=json.dumps({'msg':'No matched record found to delete'})
#             return self.render_to_http_response(json_data,status=404)
#         deleted,item_delete=obj.delete()
#         if deleted==1:
#             json_data=json.dumps({'msg':'Successfully Deleted'})
#             return self.render_to_http_response(json_data,status=200)
#         error_msg=json.dumps({'msg':'unable to delete plz try again'})
#         return self.render_to_http_response(json_data,status=500)

class EmployeeCRUDCBV(SerializeMixin,HttpResponseMixin, View):
    def get_object_by_id(self,id=None):
        try:
            obj=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            obj=None
        return obj

    def get(self,request,*args,**kwargs):
        valid_json= is_validjson(request.body)
        if not valid_json:
            error_msg=json.dumps({'msg':'please valid json only'})
            return self.render_to_http_response(error_msg,status=400)
        data=json.loads(request.body)
        id=data.get('id',None)
        if id is not None:
            obj=self.get_object_by_id(id)
            if obj is None:
                json_data=json.dumps({'msg':'No Matched Resource Found with specified Id'})
                return self.render_to_http_response(json_data,status=400)
            else:
                json_data= self.serialize([obj])
                return self.render_to_http_response(json_data)

        qs=Employee.objects.all()
        json_data=self.serialize(qs)
        return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs):
        valid_json= is_validjson(request.body)
        if not valid_json:
            error_msg=json.dumps({'msg':'please valid json only'})
            return self.render_to_http_response(error_msg,status=400)
        data=json.loads(request.body)
        form=EmployeeForm(data)
        if form.is_valid():
            obj=form.save(commit=True)
            json_data=self.serialize([obj,])
            return self.render_to_http_response(json_data,status=201)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
    def put(self,request,*args,**kwargs):
        valid_json= is_validjson(request.body)
        if not valid_json:
            error_msg=json.dumps({'msg':'please valid json only'})
            return self.render_to_http_response(error_msg,status=400)
        data=json.loads(request.body)
        id=data.get('id',None)
        if id is None:
            json_data=json.dumps({'msg':'To perform update you should provide id'})
            return self.render_to_http_response(json_data,status=400)
        obj=self.get_object_by_id(id)
        if obj is None:
            json_data=json.dumps({'msg':'No Matched Resource Found with specified Id'})
            return self.render_to_http_response(json_data,status=400)
        data=json.loads(request.body)
        current_emp={
        'eno':obj.eno,
        'ename':obj.ename,
        'esal':obj.esal,
        'eaddr':obj.eaddr,
        }
        # for key,value in data.items():
        #     current_emp[key]=value
        current_emp.update(data)
        form=EmployeeForm(current_emp,instance=obj)
        if form.is_valid():
            obj=form.save(commit=True)
            json_data=self.serialize([obj,])
            return self.render_to_http_response(json_data,status=201)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
    def delete(self,request,*args,**kwargs):
        valid_json= is_validjson(request.body)
        if not valid_json:
            error_msg=json.dumps({'msg':'please valid json only'})
            return self.render_to_http_response(error_msg,status=400)
        data=json.loads(request.body)
        id=data.get('id',None)
        if id is None:
            json_data=json.dumps({'msg':'To perform update you should provide id'})
            return self.render_to_http_response(json_data,status=400)
        obj=self.get_object_by_id(id)
        if obj is None:
            json_data=json.dumps({'msg':'No Matched Resource Found with specified Id'})
            return self.render_to_http_response(json_data,status=400)
        deleted,item_delete=obj.delete()
        if deleted==1:
            json_data=json.dumps({'msg':'Successfully Deleted'})
            return self.render_to_http_response(json_data,status=200)
        error_msg=json.dumps({'msg':'unable to delete plz try again'})
        return self.render_to_http_response(json_data,status=500)
