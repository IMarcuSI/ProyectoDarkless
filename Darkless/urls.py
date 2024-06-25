from ProyectoDarkless.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hombre", views.hombre, name="hombre"),
    path("todoCatalogo", views.todoCatalogo, name="todoCatalogo"),
    path("carro", views.carro, name="carro"),
    path("cuenta", views.cuenta, name="cuenta"),
    path("hombre", views.hombre, name="hombre"),
    path("mujer", views.mujer, name="mujer"),
    path("curd", views.crud, name="crud"),
]


