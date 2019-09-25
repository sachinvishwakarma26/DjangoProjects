from django.shortcuts import render
from testapp.models import Album,Musician
from testapp.serializers import AlbumSerializer,MusicianSerializer
from rest_framework import generics
# Create your views here
class MusicianListView(generics.ListCreateAPIView):
    queryset=Musician.objects.all()
    serializer_class=MusicianSerializer
class MusicianView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Musician.objects.all()
    serializer_class=MusicianSerializer

class AlbumListView(generics.ListCreateAPIView):
    queryset=Album.objects.all()
    serializer_class=AlbumSerializer
class AlbumView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Album.objects.all()
    serializer_class=AlbumSerializer
