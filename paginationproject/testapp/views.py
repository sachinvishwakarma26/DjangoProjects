from django.shortcuts import render
from rest_framework.views import APIView
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.
# class EmployeeListAPIView(APIView):
#     def get(self,request,format=None):
#         qs=Employee.objects.all()
#         serializer=EmployeeSerializer(qs,many=True)
#         return Response(serializer.data)
from rest_framework.pagination import PageNumberPagination
class MyPagination(PageNumberPagination):
    page_size=10
    page_query_param='mypage'
    page_size_query_param='num'
    max_page_size=30
    last_page_strings=('the_end',)
from rest_framework.pagination import CursorPagination,LimitOffsetPagination
class MyPagination2(LimitOffsetPagination):
    default_limit=5
    limit_query_param='mylimit'

class MyPagination3(CursorPagination):
    page_size=6
    ordering='esal'


class EmployeeAPIView(generics.ListAPIView):
    queryset          =Employee.objects.all()
    serializer_class  =EmployeeSerializer
    search_fields=('^eno','ename')
    ordering_fields=('esal',)
