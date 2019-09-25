from django.contrib import admin
from testapp.models import Musician,Album
class MusicianAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','instrument')
class AlbumAdmin(admin.ModelAdmin):
    list_display=('id','name','release_date','rating','artist')

admin.site.register(Musician,MusicianAdmin)
admin.site.register(Album,AlbumAdmin)
