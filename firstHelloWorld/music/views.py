# from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from django.template import loader
from .models import Album


def index(request):
    # return HttpResponse('<h1>HOLA</h1>')
    allAlbums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    context = {'allAlbums': allAlbums}
    # return HttpResponse(template.render(context, request))

# def index(request):
# return render(request, 'firstHelloWorld/music/page.html')
    # def index(request):
    # return render(request, 'firstHelloWorld/music/page.html')
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    return HttpResponse("<h2>details from album id: "
                        + str(album_id) + "</h2>")
    return HttpResponse("<h2>details from album id: " +
                        str(album_id) + "</h2>")
