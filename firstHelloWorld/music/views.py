# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>HOLA</h1>')

# def index(request):
# return render(request, 'firstHelloWorld/music/page.html')


def detail(request, album_id):
    return HttpResponse("<h2>details from album id: "
                        + str(album_id) + "</h2>")
