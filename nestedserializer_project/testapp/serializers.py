from testapp.models import  Album,Musician
from rest_framework import serializers
class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model=Album
        fields='__all__'
class MusicianSerializer(serializers.ModelSerializer):
    album_musician=AlbumSerializer(read_only=True,many=True)
    class Meta:
        model=Musician
        # fields=('first_name','last_name','instrument','album_musician')
        fields='__all__'
