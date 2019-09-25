from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import NameSerializer
class TestApiView(APIView):
    def get(self,request,format=None):
        colors=['RED','BLUE','GREEN']
        return Response({'msg':'Color Resposne','colors':colors})
    def post(self,request):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello'+name
            return Response({'msg':message})
        return Response(serializer.errors,status=400)
    def put(self,request,pk=None):
        return Response({'method':'put'})
    def patch(self,request,pk=None):
        return Response({'method':'patch'})
    def delete(self,request,pk=None):
        return Response({'method':'delete  '})
from rest_framework import viewsets
class TestViewSet(viewsets.ViewSet):
    def list(self,request):
        colors=['RED','BLUE','GREEN']
        return Response({'msg':'Hello','colors':colors})
    def create(self,request):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello'+name
            return Response({'msg':message})
        return Response(serializer.errors,status=400)
    def retrieve(self,request,pk=None):
        return Response({'msg':'Response from retrieve method'})
    def update(self,request,pk=None):
        return Response({'msg':'Response from update method'})
    def partial_update(self,request,pk=None):
        return Response({'msg':'Response from partial_update method'})
    def destroy(self,request,pk=None):
        return Response({'msg':'Response from destroy method'})
