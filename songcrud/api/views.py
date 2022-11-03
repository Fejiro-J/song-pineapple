from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from .serializers import SongSerializer
from musicapp.models import Song
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def api_song(request):
    if request.method == 'GET':
        song = Song.objects.all()
        serializer = SongSerializer(song,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response(serializer.data)    



@api_view(['GET','PUT','DELETE'])
def api_songs(request,pk):
    song = get_object_or_404(Song,song_id=pk)
    if request.method == 'GET':        
        serializer = SongSerializer(song)
        return Response(serializer.data) 

    if request.method == 'PUT':
        serializer = SongSerializer(song,data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)

        return Response(serializer.data)

    if request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

    
