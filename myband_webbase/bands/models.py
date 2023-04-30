from django.db import models

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=200)
    rating = models.IntegerField(null=True, default=5)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField('Album Name', max_length=200)
    year = models.IntegerField()
    rating = models.IntegerField(null=True, default=5)
    songs = models.ManyToManyField(Song)

    cover_image = models.ImageField(null=False, blank=False, upload_to='images/', default='image')

    def __str__(self):
        return self.name
    

class MyUser(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(default='examp@le.com')
    suggested_password = models.CharField(max_length=200, default='Mkl12mmNd-3')

    def __str__(self):
        return self.username
    

class BandMember(models.Model):
    name = models.CharField(max_length=200)
    instruments = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Band(models.Model):
    name = models.CharField('Band Name', max_length=200)
    genres = models.CharField('Genres', max_length=200)
    active_from = models.IntegerField()
    active_to = models.IntegerField()
    still_active = models.BooleanField(default=True)
    listen_on_spotify = models.URLField('Listen to')
    members = models.ManyToManyField(BandMember)
    albums_out = models.ManyToManyField(Album, blank=True)

    band_image = models.ImageField(null=False, blank=False, upload_to="images/", default='image')
    creator = models.IntegerField(null=False, blank=False, default=1)

    def __str__(self):
        return self.name
    
