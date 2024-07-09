from ProyectoDarkless.urls import path
from Darkless import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hombre", views.hombre, name="hombre"),
    path("todoCatalogo", views.todoCatalogo, name="todoCatalogo"),
    path("carro", views.carro, name="carro"),
    path("hombre", views.hombre, name="hombre"),
    path("mujer", views.mujer, name="mujer"),
    path("crud", views.crud, name="crud"),
    path("login", views.conectar, name="login"),
    path("logout", views.desconectar, name="logout"),
    path("user_add", views.user_add, name="user_add"),
    path("user_update", views.user_update, name="user_update"),
    path("user_del/<str:pk>", views.user_del, name="user_del"),
    path("user_findEdit/<str:pk>", views.user_findEdit, name="user_findEdit"),
    path("user_update", views.user_update, name="user_update"),
    path("crud_genero", views.crud_genero, name="crud_genero"),
    path("genero_add", views.genero_add, name="genero_add"),
    path("genero_del/<str:pk>", views.genero_del, name="genero_del"),
    path("genero_edit/<str:pk>", views.genero_edit, name="genero_edit"),
    path("crud_tipo", views.crud_tipo, name="crud_tipo"),
    path("tipo_add", views.tipo_add, name="tipo_add"),
    path("tipo_del/<str:pk>", views.tipo_del, name="tipo_del"),
    path("crud_ropa2", views.crud_ropa2, name="crud_ropa2"),
    path("ropa2_add", views.ropa2_add, name="ropa2_add"),
    path("tipo_edit/<str:pk>", views.tipo_edit, name="tipo_edit"),
    path("ropa2_update", views.ropa2_update, name="ropa2_update"),
    path("ropa2_del/<str:pk>", views.ropa2_del, name="ropa2_del"),
    path("ropa2_findEdit/<str:pk>", views.ropa2_findEdit, name="ropa2_findEdit"),

]


