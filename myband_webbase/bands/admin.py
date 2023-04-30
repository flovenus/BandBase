from django.contrib import admin

# Register your models here.
from .models import Band
from .models import BandMember
from .models import Album
from .models import Song
from .models import MyUser

admin.site.register(Band)
admin.site.register(BandMember)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(MyUser)