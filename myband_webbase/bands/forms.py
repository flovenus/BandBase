from django import forms
from django.forms import ModelForm
from .models import Song
from .models import Band
from .models import Album
from .models import BandMember
from .models import MyUser

# Create your Forms
class BandForm(ModelForm):
    class Meta:
        model = Band
        fields = ('name', 'genres', 'active_from', 'active_to', 'still_active', 'listen_on_spotify', 'band_image')
        labels = {
            'band_image': 'Picture of the Band (.png/.jpg)',
        }

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'year', 'cover_image')
        labels = {
            'cover_image': 'Album cover (.png/.jpg)',
        }

class MemberForm(ModelForm):
    class Meta:
        model = BandMember
        fields = ('name', 'instruments')

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ('name', )

class UserForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'suggested_password')