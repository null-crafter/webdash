from django.urls import path

from . import views

urlpatterns = [
    path("", views.index,),
    path("background-image/", views.background_image),
]
