from django.db import models
from django.core.serializers import serialize
import json

class EmployeeManager(models.Manager):
    def get_queryset(self):
        qs=super().get_queryset()
        json_data=serialize('json',qs,fields=('eno','ename'))
        struct=json.loads(json_data)
        final_array=[]
        for obj in struct:
            final_array.append(obj['fields'])
        data=json.dumps(final_array)
        return data

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=64)
    
