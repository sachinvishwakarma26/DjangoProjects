from rest_framework import serializers
from testapp.models import Employee
class EmployeeSerializer(serializers.Serializer):
    eno=serializers.IntegerField()
    ename=serializers.CharField(max_length=64)
    esal=serializers.FloatField()
    eaddr=serializers.CharField(max_length=64)
    def validate_esal(self,value):
        print('field level validation')
        if value<5000:
            raise serializers.ValidationError('The salary should be minimum 5000')
        return value
    def validate(self,data):
        print('global validation')
        esal=data.get('esal')
        ename=data.get('ename')
        if esal<5000:
            raise serializers.ValidationError('The salary should be minimum 5000')
        if ename[0].lower() !='s':
            raise serializers.ValidationError('The ename should starts with S, like Sunny')
        return data


    def create(self,validated_data):
        return Employee.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.eno=validated_data.get('eno',instance.eno)
        instance.ename=validated_data.get('ename',instance.ename)
        instance.esal=validated_data.get('esal',instance.esal)
        instance.eaddr=validated_data.get('eaddr',instance.eaddr)
        instance.save()
        return instance
