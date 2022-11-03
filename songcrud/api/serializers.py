from rest_framework import serializers
from musicapp.models import Song,Artiste



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__' 


