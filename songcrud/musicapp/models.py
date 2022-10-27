from django.db import models
import uuid
# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()


    def __str__(self):
        return f'{self.last_name},{self.first_name}'


class Song(models.Model):
    title = models.CharField(max_length=100)
    date_released = models.DateField()
    #likes = 
    artiste_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    artist = models.ForeignKey('Artiste',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title



class Lyrics(models.Model):
    content = models.TextField(max_length=600)
    song_id = models.OneToOneField(Song,on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return self.content