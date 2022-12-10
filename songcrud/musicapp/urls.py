from django.urls import path 
from . import views
app_name = 'musicapp'

urlpatterns = [
    path('new', views.new_view)


]