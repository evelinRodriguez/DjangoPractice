# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Album


def index(request):
    allAlbums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all albums': allAlbums,
    }
    return HttpResponse(template.render(context, request))

# def index(request):
# return render(request, 'firstHelloWorld/music/page.html')


def detail(request, album_id):
    return HttpResponse("<h2>details from album id: "
                        + str(album_id) + "</h2>")
