from django.shortcuts import render,redirect
from rest_framework.views import APIView
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth import authenticate,login
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# def login_form(request):
#     return render(request,'testapp/login.html')
#
# def login_user(request):
#     username=request.POST.get('uname')
#     password=request.POST.get('pwd')
#     user=authenticate(username=username,password=password)
#     if user is not None:
#         login(request,user)
#         return redirect('/api')
#     else:
#         return redirect('/auth')

# Create your views here.
# class EmployeeListAPIView(APIView):
#     def get(self,request,format=None):
#         qs=Employee.objects.all()
#         serializer=EmployeeSerializer(qs,many=True)
#         return Response(serializer.data)
from testapp.pagination import MyPagination3
class EmployeeAPIView(generics.ListAPIView):
    queryset          =Employee.objects.all()
    serializer_class  =EmployeeSerializer
    search_fields=('ename',)
    ordering_fields=('eno','esal')
    # def get_queryset(self):
    #     qs=Employee.objects.all()
    #     name=self.request.GET.get('ename')
    #     if name is not None:
    #         qs=qs.filter(ename__icontains=name)
    #     return qs
