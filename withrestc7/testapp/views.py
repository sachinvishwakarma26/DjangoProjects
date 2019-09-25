from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from  rest_framework.viewsets import ModelViewSet
# Create your views here.
class EmployeeViewSet(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset        =Employee.objects.all()
