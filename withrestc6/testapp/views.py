from django.shortcuts import render
from rest_framework.views import APIView
from testapp.serializers import EmployeeSerializer
from rest_framework.response import Response
from testapp.models import Employee
from rest_framework import generics
# Create your views here.
# class EmployeeListAPIView(APIView):
#     def get(self,request,format=None):
#         qs=Employee.objects.all()
#         serializer=EmployeeSerializer(qs,many=True)
#         return Response(serializer.data)
#
# from rest_framework import generics
# class EmployeeAPIView(generics.ListAPIView):
#     # queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     def get_queryset(self):
#         qs=Employee.objects.all()
#         name=self.request.GET.get('ename')
#         if name is not None:
#             qs=qs.filter(ename__icontains=name)
#         return qs
# class EmployeeCreateAPIView(generics.CreateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
# class EmployeeDetailAPIView(generics.RetrieveAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='id'
# class EmployeeUpdateAPIView(generics.UpdateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='id'
# class EmployeeDeleteAPIView(generics.DestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='id'
# class EmployeeListCreateAPIView(generics.ListCreateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
# class EmployeeRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='id'
# class EmployeeRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='id'
# class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='id'

from rest_framework import mixins
class EmployeeListModelMixin(mixins.CreateModelMixin,generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class EmployeeDetailAPIViewMixin(mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
