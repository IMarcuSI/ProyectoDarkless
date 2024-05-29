from ProyectoDarkless.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hombre", views.hombre, name="hombre"),
]

