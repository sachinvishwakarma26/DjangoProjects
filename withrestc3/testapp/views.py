from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import NameSerializer
# Create your views here.
class TestApiView(APIView):
    def get(self,request,format=None):
        colors=['RED','BLUE','GREEN','YELLOW','INDIGO']
        return Response({'msg':'Welcome to Colorful Year','colors':colors})
    def post(self,request):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {} Wish You Happy New Year !!!'.format(name)
            return Response({'msg':msg})
        return Response(serializer.errors,status=400)
    def put(self,request,pk=None):
        return Response({'msg':'Response from put method'})
    def patch(self,request,pk=None):
        return Response({'msg':'Response from patch method'})
    def delete(self,request,pk=None):
        return Response({'msg':'Response from delete method'})

from rest_framework import viewsets
class TestViewSet(viewsets.ViewSet):
    def list(self,request):
        colors=['RED','GREEN','YELLOW','ORANGE']
        return Response({'msg':'Wish YOu Colorful Life in 2019','colors':colors})
    def create(self,request):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {} Your Life will be settled in 2019'.format(name)
            return Response({'msg':msg})
        return Response(serializer.errors,status=400)
    def retrieve(self,request,pk=None):
        return Response({'msg':'Response from retrieve method'})
    def update(self,request,pk=None):
        return Response({'msg':'Response from update method'})
    def partial_update(self,request,pk=None):
        return Response({'msg':'Response from partial_update method'})
    def destroy(self,request,pk=None):
        return Response({'msg':'Response from destroy method'})
