from .models import Album
from django.shortcuts import render
from django.http import Http404


def index(request):
    allAlbums = Album.objects.all()
    context = {'allAlbums': allAlbums}
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("album does not exist")
    return render(request, 'music/detail.html', {'album': album})
