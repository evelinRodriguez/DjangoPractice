# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Album


def index(request):
    allAlbums = Album.objects.all()
    html = ''
    for album in allAlbums:
        # esto es para que en urls.py reconoza el link
        url = str(album.id) + '/'
        # aqui va a poner cada una de las urls creadas con el titulo del album
        html += '<a href="' + url + '">' + album.albumTitle + '</a><br>'
    return HttpResponse(html)

# def index(request):
# return render(request, 'firstHelloWorld/music/page.html')


def detail(request, album_id):
    return HttpResponse("<h2>details from album id: "
                        + str(album_id) + "</h2>")
