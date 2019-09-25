from rest_framework import serializers
class TestSerializer(serializers.Serializer):
    heroname=serializers.CharField(max_length=10)
