from django.urls import path
from . import views

urlpatterns = [
    path('songs/',views.api_song),
    path('songs/<str:pk>',views.api_songs)
]