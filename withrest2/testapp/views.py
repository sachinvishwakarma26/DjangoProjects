from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import TestSerializer
from rest_framework import status
class TestApiView(APIView):
    serializer_class=TestSerializer
    def get(self,request,format=None):
        colors=['RED','BLUE','GREEN','YELLOW']
        return Response({'msg':'Hello','colors':colors})
    def post(self,request):
        serializer=TestSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('heroname')
            msg='Hello '+name
            return Response({'msg':msg})
        return Response(serializer.errors,status=400)
    def put(self,request,pk=None):
        return Response({'method':'put'})

    def patch(self,request,pk=None):
        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        return Response({'method':'delete'})
