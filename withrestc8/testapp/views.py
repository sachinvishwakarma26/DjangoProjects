from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
class EmployeeCRUDCBV(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
    authentication_classes=[JSONWebTokenAuthentication,]
    permission_classes=[IsAuthenticated,]
