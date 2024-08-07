from django.shortcuts import render
from .models import Genero,Usuario,Ropa2,Tipo
from .forms import GeneroForm,UsuarioForm,Ropa2Form ,TipoForm
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
@login_required
def carro(request):

  context = {}

  return render(request, "pages/carro.html", context)

def hombre(request):

  context = {}

  return render(request, "pages/hombre.html", context)

def mujer(request):

  context = {}

  return render(request, "pages/mujer.html", context)

@login_required
def crud_ropa2(request):
    ropas = Ropa2.objects.all()
    context = {
        "ropas": ropas,
    }
    return render(request, "pages/crud_ropa2.html", context)
@login_required
def crud(request):
    usuarios = Usuario.objects.all()
    context = {
        "usuarios": usuarios,
    }
    return render(request, "pages/crud.html", context)
@login_required
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

        objGenero = Genero.objects.get(id_genero=genero)

        obj = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=appPaterno,
            apellido_materno=appMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,
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
        generos = Genero.objects.all()

        context={
            "usuario":usuario,
            "generos":generos,
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
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        correo = request.POST["correo"]
        password = request.POST["password"]
        direccion = request.POST["direccion"]
        activo = True

        """ Obtengo genero desde la BDD para modificar """
        objGenero = Genero.objects.get(id_genero=genero)

        """ Genero la instancia """

        obj = Usuario(
            rut=rut,
            nombre=nombre,
            apellido_paterno=appPaterno,
            apellido_materno=appMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,
            telefono=telefono,
            email=correo,
            password=password,
            direccion=direccion,
            activo=activo,
        )
        obj.save()

        generos = Genero.objects.all()
        context = {
            "mensaje": "Modificado con Exito",
            "generos":generos,
            "usuario":obj,
        }
        return render(request, "pages/user_update.html", context)

@login_required
def crud_genero(request):
    generos = Genero.objects.all()

    context={
        "generos":generos,
    }
    return render(request,"pages/crud_genero.html",context)
@login_required
def genero_add(request):
    formGenero = GeneroForm()
    formUsuario = UsuarioForm()
    if request.method=="POST":
        nuevo = GeneroForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()

            context={
                "mensaje":"Agregado con exito",
                "form":formGenero
            }
            return render(request,"pages/genero_add.html",context)
    else:
        context = {
            "form":formGenero,
            "form2":formUsuario
        }
        return render(request,"pages/genero_add.html",context)

def genero_del(request,pk):
    try:
        genero = Genero.objects.get(id_genero=pk)
        genero.delete()

        generos = Genero.objects.all()
        context={
            "mensaje":"Registro eliminado exitosamente",
            "generos":generos
        }
        return render(request,"pages/crud_genero.html",context)
    except:
        generos = Genero.objects.all()
        context={
            "mensaje":"Error, Genero no encontrado...",
            "generos":generos
        }
        return render(request,"pages/crud_genero.html",context)

def genero_edit(request,pk):
    if pk!="":
        genero = Genero.objects.get(id_genero=pk)
        form = GeneroForm(instance=genero)
        if request.method=="POST":
            nuevo = GeneroForm(request.POST,instance=genero)

            if nuevo.is_valid():
                nuevo.save()

                context ={
                    "mensaje":"Modificado con exito",
                    "form":nuevo
                }
                return render(request,"pages/genero_edit.html",context)
        else:
            context={
                "form":form,
            }
            return render(request,"pages/genero_edit.html",context)
    else:
        generos = Genero.objects.all()
        context={
            "mensaje":"Error, genero no encontrado",
            "generos":generos
        }
        return render(request,"pages/crud_genero.html",context)

def loginSession(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username == "marcus" and password=="pass123":
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
            return render(request,"pages/login.html",context)
    else:
        context = {
        }
        return render(request,"pages/login.html",context)

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
            return render(request,"pages/login.html",context)
    else:
        #Corresponde a redireccionar
        context = {
        }
        return render(request,"pages/login.html",context)

def desconectar(request):
    #del request.session["user"]
    logout(request)
    context = {
        "mensaje":"Sesion cerrada",
        "design":"alert alert-info w-50 mx-auto text-center",
    }
    return render(request,"pages/login.html",context)
@login_required
def crud_tipo(request):
    tipos = Tipo.objects.all()

    context={
        "tipos":tipos,
    }
    return render(request,"pages/crud_tipo.html",context)

def tipo_add(request):
    formTipo = TipoForm()
    formRopa2 = Ropa2Form()
    if request.method=="POST":
        nuevo = TipoForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()

            context={
                "mensaje":"Agregado con exito",
                "form":formTipo
            }
            return render(request,"pages/tipo_add.html",context)
    else:
        context = {
            "form":formTipo,
            "form2":formRopa2
        }
        return render(request,"pages/tipo_add.html",context)
    
def tipo_del(request,pk):
    try:
        tipo = Tipo.objects.get(id_tipo=pk)
        tipo.delete()

        tipos = Tipos.objects.all()
        context={
            "mensaje":"Registro eliminado exitosamente",
            "tipos":tipos
        }
        return render(request,"pages/crud_tipo.html",context)
    except:
        generos = Tipo.objects.all()
        context={
            "mensaje":"Error, tipo no encontrado...",
            "tipo":tipo
        }
        return render(request,"pages/crud_tipo.html",context)

def ropa2_add(request):
    if request.method != "POST":
        tipos = Tipo.objects.all()
        context = {
            "tipos": tipos,
        }
        return render(request, "pages/ropa2_add.html", context)
    else:
        id_ropa = request.POST["id_ropa"]
        nombre = request.POST["nombre_ropa"]
        fecha = request.POST["fecha"]
        tipo = request.POST["tipo"]
        activo = True

        objTipo = Tipo.objects.get(id_tipo=tipo)

        obj = Ropa2.objects.create(
            id_ropa=id_ropa,
            nombre_ropa=nombre,
            fecha_lazamiento=fecha,
            id_tipo=objTipo,
            activo=activo,
        )
        obj.save()
        context = {
            "mensaje": "Registro Exitoso",
        }
        return render(request, "pages/ropa2_add.html", context)

def tipo_edit(request,pk):
    if pk!="":
        tipo = Tipo.objects.get(id_tipo=pk)
        form = TipoForm(instance=tipo)
        if request.method=="POST":
            nuevo = TipoForm(request.POST,instance=tipo)

            if nuevo.is_valid():
                nuevo.save()

                context ={
                    "mensaje":"Modificado con exito",
                    "form":nuevo
                }
                return render(request,"pages/tipo_edit.html",context)
        else:
            context={
                "form":form,
            }
            return render(request,"pages/tipo_edit.html",context)
    else:
        tipos = Tipo.objects.all()
        context={
            "mensaje":"Error, tipo no encontrado",
            "tipos":tipos
        }
        return render(request,"pages/crud_.html",context)
    
def tipo_del(request,pk):
    try:
        tipo = Tipo.objects.get(id_tipo=pk)
        tipo.delete()

        tipos = Tipo.objects.all()
        context={
            "mensaje":"Registro eliminado exitosamente",
            "tipos":tipos
        }
        return render(request,"pages/crud_tipo.html",context)
    except:
        tipos= Tipo.objects.all()
        context={
            "mensaje":"Error, Tipo no encontrado...",
            "tipos":tipos
        }
        return render(request,"pages/crud_tipo.html",context)
    
def ropa2_findEdit(request,pk):
    if pk!="":
        """ 
            objects.get() = Obtener datos con filtro
            objects.all() = Obtener todos
        """
        ropa2 = Ropa2.objects.get(id_ropa=pk)
        tipos = Tipo.objects.all()

        context={
            "ropa2":ropa2,
            "tipos":tipos,
        }
        return render(request,"pages/ropa2_update.html",context)
    else:
        ropas = Ropa2.objects.all()
        context={
            "mensaje":"Error,id no encontrado",
            "ropa2":ropa2
        }
        return render(request,"pages/crud_ropa2.html",context)
    
def ropa2_del(request, pk):
    try:
        ropa2 = Ropa2.objects.get(rut=pk)
        ropa2.delete()

        ropas = Ropa2.objects.all()
        context = {
            "mensaje": "Registro Eliminado",
            "ropas": ropas,
        }
        return render(request, "pages/crud_ropa2.html", context)
    except:
        ropas = Ropa2.objects.all()
        context = {
            "mensaje": "Error,Rut no encontrado...",
            "ropas": ropas,
        }
        return render(request, "pages/crud_ropas.html", context)
    
def ropa2_update(request):
    if request.method=="POST":
        """ 
            Capturo todos los datos del front
            Identificamos
            Asignamos nombre 
        """
        id_ropa = request.POST["id_ropa"]
        nombre_ropa = request.POST["nombre_ropa"]
        fecha = request.POST["fecha"]
        tipo = request.POST["tipo"]
        activo = True
        """ Obtengo genero desde la BDD para modificar """
        objtipo = Tipo.objects.get(id_tipo=tipo)

        """ Genero la instancia """

        obj = Ropa2(
        id_ropa = id_ropa,
        nombre_ropa = nombre_ropa,
        fecha = fecha,
        tipo = tipo,
        activo = True,
        )
        obj.save()

        tipos = Tipo.objects.all()
        context = {
            "mensaje": "Modificado con Exito",
            "tipos":tipos,
            "ropa2":obj,
        }
        return render(request, "pages/user_update.html", context)
