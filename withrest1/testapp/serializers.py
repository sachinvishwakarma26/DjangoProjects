from rest_framework import serializers
from testapp.models import Employee

class EmployeeSerializer(serializers.Serializer):
    eno=serializers.IntegerField()
    ename=serializers.CharField(max_length=64)
    esal=serializers.FloatField()
    eaddr=serializers.CharField(max_length=64)

    def create(self,validated_data):
        return Empoyee.objects.create(**validated_data)
