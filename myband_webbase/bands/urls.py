from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('browse_bands', views.all_bands, name='list-bands'),
    path('add_band', views.add_band, name='add_band'),
    path('personal_lists', views.personal_lists, name='personal_lists'),

    path('band_page/add_album/<band_id>', views.add_album, name='add_album'),
    path('band_page/<band_id>', views.band_page, name='show_band'),
    path('band_page/album_page/<album_id>', views.album_page, name='show_album'),

    path('delete_album<album_id>', views.delete_album, name='delete_album'),
    path('delete_band/<band_id>', views.delete_band, name='delete_band'),
    path('delete_member/<member_id>', views.delete_member, name='delete_member'),
    path('delete_song/<song_id>', views.delete_song, name='delete_song'),

    path('search', views.search, name='search'),
    path('about', views.about, name='about')
]
