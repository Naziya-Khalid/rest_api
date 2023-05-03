from rest_framework import serializers
from .models import Work, Artist

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['link', 'work_type', 'artist']

class ArtistSerializer(serializers.ModelSerializer):
    works = WorkSerializer(many=True)

    class Meta:
        model = Artist
        fields = ['name', 'works']

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=128, write_only=True)