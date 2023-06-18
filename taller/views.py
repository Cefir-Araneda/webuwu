from django.shortcuts import render
from .models import Mecanico, Genero, Mantencion, Atencion
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

def register(request):
    if request.method != "POST":
        Users= User.objects.all()
        context={'Users':Users}
        return render(request, 'taller/signup.html', context)
    else:
        newuser=request.POST["newuser"]
        pass1=request.POST["password1"]
        pass2=request.POST["password2"]
        mail=request.POST["email"]

        if pass1 == pass2:
            obj=User.objects.create_user(username=newuser,
                                         password=pass1,
                                         email=mail)
            obj.save()
            Users= User.objects.all()
            context={'Users':Users}
            return render(request, 'taller/home.html', context)        
    print("Las contraseñas ingresadas son distintas")
    return render(request, 'taller/signup.html')

@login_required
def menu(request):
    context={}
    if request.user.is_authenticated:
        request.session["username"]=request.user.username
        usuario=request.session["username"]
        context={'usuario':usuario}
    return render(request,'taller/menu.html',context)

def home(request):
    context={}
    return render(request, 'taller/home.html', context)

def perfil(request):
    context={}
    return render(request, 'taller/perfil.html', context)

def trabajosrecientes(request):
    context={}
    return render(request, 'taller/perfil.html', context)

def categoria(request):
    context={}
    return render(request, 'taller/categoria.html', context)

def mecanico(request):
    context={}
    return render(request, 'taller/mecanico.html', context)

def contactanos(request):
    context={}
    return render(request, 'taller/contactanos.html', context)


def trabajo1(request):
    context={}
    return render(request, 'taller/trabajo1.html', context)

def trabajo2(request):
    context={}
    return render(request, 'taller/trabajo2.html', context)

def trabajo3(request):
    context={}
    return render(request, 'taller/trabajo3.html', context)

def mantenciones(request):
    context={}
    return render(request, 'taller/mantenciones.html', context)

def notificaciones(request):
    context={}
    return render(request, 'taller/notificaciones.html', context)

# CRUD Agregar Atencion

def index(request):
    mecanicos= Mecanico.objects.all()
    context={"mecanicos":mecanicos}
    return render(request, 'taller/index.html', context)

def crud(request):
    atenciones= Atencion.objects.all()
    context= {'atenciones': atenciones}
    return render(request, 'taller/atenciones_list.html', context) 

@login_required
def atencionesAdd(request):
    if request.method != "POST":
        mecanicos= Mecanico.objects.all()
        mantenciones= Mantencion.objects.all()
        context={'mecanicos':mecanicos,'mantenciones':mantenciones}
        return render(request, 'taller/atenciones_add.html', context)
    else:
        mecanico=request.POST["mecanico"]
        fechaAte=request.POST["fechaAte"]
        modelo=request.POST["modelo"]
        patente=request.POST["patente"]
        diagnostico=request.POST["diagnostico"]
        mantencion=request.POST["mantencion"]
        cantidad=request.POST["cantidad"]
        valor=request.POST["valor"]

        objMecanico=Mecanico.objects.get(rut = mecanico)
        objMantencion=Mantencion.objects.get(id_mantencion = mantencion)
        obj=Atencion.objects.create(    mecanico=objMecanico,
                                        fecha_atencion=fechaAte,
                                        modelo=modelo,
                                        patente=patente,
                                        diagnostico=diagnostico,
                                        id_mantencion=objMantencion,
                                        cantidad=cantidad,
                                        valor=valor)
        obj.save()
        mecanicos= Mecanico.objects.all()
        mantenciones= Mantencion.objects.all()
        context={'mecanicos':mecanicos,'mantenciones':mantenciones,'mensaje':"Ok, Atencion registrada..."}
        return render(request, 'taller/atenciones_add.html', context)

@login_required
def atenciones_del(request,pk):
    context={}
    try:
        atencion=Atencion.objects.get(id_atencion=pk)

        atencion.delete()
        mensaje="Bien, datos eliminados..."
        atenciones= Atencion.objects.all()
        context= {'atenciones': atenciones, 'mensaje': mensaje}
        return render(request, 'taller/atenciones_list.html', context)
    except:
        mensaje="Error, atencion no existe..."
        atenciones= Atencion.objects.all()
        context= {'atenciones': atenciones, 'mensaje': mensaje}
        return render(request, 'taller/atenciones_list.html', context)
    
@login_required
def atenciones_editFind(request,pk):
    if pk != "":
        atenciones= Atencion.objects.get(id_atencion=pk)
        mecanicos=Mecanico.objects.all()
        mantenciones= Mantencion.objects.all()

        context= {'atenciones': atenciones, 'mecanicos': mecanicos,'mantenciones': mantenciones}
        if atenciones:
            return render(request, 'taller/atenciones_edit.html', context)
        else:
            context= {'mensaje': "Error, atencion no existe..."}
            return render(request, 'taller/atenciones_list.html', context)

@login_required
def atencionesUpdate(request):
    if request.method == "POST":

        id_ate=request.POST["id_ate"]
        mecanico=request.POST["mecanico"]
        fechaAte=request.POST["fechaAte"]
        modelo=request.POST["modelo"]
        patente=request.POST["patente"]
        diagnostico=request.POST["diagnostico"]
        mantencion=request.POST["mantencion"]
        cantidad=request.POST["cantidad"]
        valor=request.POST["valor"]
        
        objMecanico=Mecanico.objects.get(rut = mecanico)
        objMantencion=Mantencion.objects.get(id_mantencion = mantencion)

        atencion = Atencion()
        atencion.id_atencion=id_ate
        atencion.mecanico=objMecanico
        atencion.fecha_atencion=fechaAte
        atencion.modelo=modelo
        atencion.patente=patente
        atencion.diagnostico=diagnostico
        atencion.id_mantencion=objMantencion
        atencion.cantidad=cantidad
        atencion.valor=valor
        atencion.save()
        
        mecanicos=Mecanico.objects.all()
        mantenciones= Mantencion.objects.all()
        context={'mensaje':"Ok, datos actualizados...",'mecanicos': mecanicos,'mantenciones': mantenciones, 'atencion': atencion}
        return render(request, 'taller/atenciones_edit.html',context)
    else:
        atenciones = Atencion.objects.all()
        context={'atenciones':atenciones}
        return render(request, 'taller/atencion_list.html',context)