from django.shortcuts import render
from .models import Band
from .models import BandMember
from .models import Album
from .models import Song
from .forms import BandForm
from .forms import MemberForm
from .forms import AlbumForm
from .forms import SongForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
def home(request):
    return redirect('/browse_bands')

def all_bands(request):
    band_list = Band.objects.all()
    return render(request, 'bands/all_bands.html', {'band_list': band_list})

def add_band(request):
    submitted = False
    if request.method == "POST":
        form = BandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_band?submitted=True')
    else:
        form = BandForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'bands/add_band.html', {'form':form, 'submitted':submitted})


def add_album(request, band_id):
    band = Band.objects.get(pk=band_id)
    submitted = False
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)

        bandmembers = band.members.all()
        if form.is_valid():
            form.save()
            album = Album.objects.latest('id')
            band.albums_out.add(album)
            albums = band.albums_out.all().order_by('year').values()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = AlbumForm(request.POST)
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'bands/add_album.html', {'form': form, 'submitted': submitted, 'band': band})


def band_page(request, band_id):
    band = Band.objects.get(pk=band_id)
    bandmembers = band.members.all()
    albums = band.albums_out.all().order_by('year').values()

    form = MemberForm(request.POST)
    if request.POST:
        forme = form
        if forme.is_valid():
            forme.save()
            member = BandMember.objects.latest('id')
            band.members.add(member)
            return redirect(request.META.get('HTTP_REFERER'))
    return render(request, 'bands/band_page.html', {'band': band, 'bandmembers': bandmembers, 'albums': albums, 'form': form})


def album_page(request, album_id):
    album = Album.objects.get(pk=album_id)
    songs = album.songs.all()

    form = SongForm(request.POST)
    if request.method == 'POST':
        forme = form
        if forme.is_valid():
            forme.save()
            song = Song.objects.latest('id')
            album.songs.add(song)
            return redirect(request.META.get('HTTP_REFERER'))
    return render(request, 'bands/album_page.html', {'album': album, 'songs': songs, 'form': form})


def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    songs = album.songs.all()
    songs.delete()
    album.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def delete_band(request, band_id):
    band = Band.objects.get(pk=band_id)
    albums = band.albums_out.all()
    for album in albums:
        delete_album(request, album.id)
    members = band.members.all()
    members.delete()
    band.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def delete_member(request, member_id):
    member = BandMember.objects.get(pk=member_id)
    member.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def delete_song(request, song_id):
    song = Song.objects.get(pk=song_id)
    song.delete()
    return redirect(request.META.get('HTTP_REFERER'))



def search(request):
    if request.method == 'POST':
        searchterm = request.POST['searchterm']
        bandresults = Band.objects.filter(name__contains=searchterm)
        albumresults = Album.objects.filter(name__contains=searchterm)
        return render(request, 'bands/search.html', {'searchterm': searchterm, 'bandresults': bandresults, 'albumresults': albumresults})
    else:
        return render(request, 'bands/search.html', {})
    


def personal_lists(request):
    return render(request, 'bands/personal_lists.html', {})


def about(request):
    return render(request, 'bands/about.html', {})