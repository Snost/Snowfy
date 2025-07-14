from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year = models.IntegerField()
    cover = models.URLField(blank=True)  

    def __str__(self):
        return f"{self.title} ({self.year})"

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    title = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='tracks/')
    lyrics = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.title} - {self.album.title}"

class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.album.title}"




    def __str__(self):
        return self.title
