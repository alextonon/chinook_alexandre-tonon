from django.shortcuts import render

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


def album(request, album_id):
    album_track_list = Track.objects.filter(album=album_id)
    template = loader.get_template("disks/album.html")
    context = {
        "all_album_list": all_album_list,
    }
    return HttpResponse(template.render(context, request))


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)