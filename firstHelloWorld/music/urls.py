from django.urls import path
from . import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # /music/
    path('', views.index, name='index'),
    # /music/id/
    path('<album_id>/', views.detail, name='detail'),

]

# urlpatterns += staticfiles_urlpatterns()
