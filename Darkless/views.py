from django.shortcuts import render

def index(request):
    context = {
        "usuario": "",
    }
    return render(request, "pages/index.html", context)


def todoCatalogo(request):

  context = {}

  return render(request, "pages/todoCatalogo.html", context)

def carro(request):

  context = {}

  return render(request, "pages/carro.html", context)

def cuenta(request):

  context = {}

  return render(request, "pages/cuenta.html", context)

def hombre(request):

  context = {}

  return render(request, "pages/hombre.html", context)

def mujer(request):

  context = {}

  return render(request, "pages/mujer.html", context)