from django.shortcuts import render
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context = {
        "user": "",
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

def crud(request):
    usuarios = Usuario.objects.all()
    context = {
        "usuarios": usuarios,
    }
    return render(request, "pages/crud.html", context)


def user_add(request):
    if request.method != "POST":
        generos = Genero.objects.all()
        context = {
            "generos": generos,
        }
        return render(request, "pages/user_add.html", context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fechaNac = request.POST["fecha"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        correo = request.POST["correo"]
        password = request.POST["password"]
        direccion = request.POST["direccion"]
        activo = True

        obj = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=appPaterno,
            apellido_materno=appMaterno,
            fecha_nacimiento=fechaNac,
            telefono=telefono,
            email=correo,
            password=password,
            direccion=direccion,
            activo=activo,
        )
        obj.save()
        context = {
            "mensaje": "Registro Exitoso",
        }
        return render(request, "pages/user_add.html", context)


def user_del(request, pk):
    try:
        usuario = Usuario.objects.get(rut=pk)
        usuario.delete()

        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Registro Eliminado",
            "usuarios": usuarios,
        }
        return render(request, "pages/crud.html", context)
    except:
        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Error,Rut no encontrado...",
            "usuarios": usuarios,
        }
        return render(request, "pages/crud.html", context)

def user_findEdit(request,pk):
    if pk!="":
        """ 
            objects.get() = Obtener datos con filtro
            objects.all() = Obtener todos
        """
        usuario = Usuario.objects.get(rut=pk)

        context={
            "usuario":usuario,
        }
        return render(request,"pages/user_update.html",context)
    else:
        usuarios = Usuario.objects.all()
        context={
            "mensaje":"Error,Rut no encontrado",
            "usuarios":usuarios
        }
        return render(request,"pages/crud.html",context)

def user_update(request):
    if request.method=="POST":
        """ 
            Capturo todos los datos del front
            Identificamos
            Asignamos nombre 
        """
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fechaNac = request.POST["fecha"]
        telefono = request.POST["telefono"]
        correo = request.POST["correo"]
        password = request.POST["password"]
        direccion = request.POST["direccion"]
        activo = True

        """ Genero la instancia """

        obj = Usuario(
            rut=rut,
            nombre=nombre,
            apellido_paterno=appPaterno,
            apellido_materno=appMaterno,
            fecha_nacimiento=fechaNac,
            telefono=telefono,
            email=correo,
            password=password,
            direccion=direccion,
            activo=activo,
        )
        obj.save()


        context = {
            "mensaje": "Modificado con Exito",
            "usuario":obj,
        }
        return render(request, "pages/user_update.html", context)
    

def loginSession(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username == "j.riquelmee" and password=="pass1234":
            request.session["user"] = username
            usuarios = Usuario.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/crud.html",context)
        else:
            context ={
                "mensaje":"Usuario o contraseña incorrecta",
                "design" : "alert alert-danger w-50 mx-auto text-center",
            }
            return render(request,"pages/cuenta.html",context)
    else:
        context = {
        }
        return render(request,"pages/cuenta.html",context)

def conectar(request):
    if request.method=="POST":
        #Corresponde al formulario
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            usuarios = Usuario.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/crud.html",context)
        else:
            context = {
                "mensaje":"Usuario o contraseña incorrecta",
                "design":"alert alert-danger w-50 mx-auto text-center",
            }
            return render(request,"pages/cuenta.html",context)
    else:
        #Corresponde a redireccionar
        context = {
        }
        return render(request,"pages/cuenta.html",context)

def desconectar(request):
    #del request.session["user"]
    logout(request)
    context = {
        "mensaje":"Sesion cerrada",
        "design":"alert alert-info w-50 mx-auto text-center",
    }
    return render(request,"pages/cuenta.html",context)
