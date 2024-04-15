from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Track
from .models import Album
from .models import Artist

def index(request):
    all_album_list = Album.objects.all()
    template = loader.get_template("disks/index.html")
    context = {
        "all_album_list": all_album_list,
    }
    return HttpResponse(template.render(context, request))


def album(request, title):
    album = get_object_or_404(Album, title=title)
    album_track_list = Track.objects.filter(album=album.id)
    template = loader.get_template("disks/album.html")
    context = {
        "album_track_list": album_track_list,
    }
    return HttpResponse(template.render(context, request))