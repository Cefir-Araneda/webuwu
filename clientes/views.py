from django.shortcuts import render
from .models import Mecanico, Genero, Mantencion, Atencion
from .forms import GeneroForm, AtencionForm

# Create your views here.

def index(request):
    mecanicos= Mecanico.objects.all()
    context={"mecanicos":mecanicos}
    return render(request, 'clientes/index.html', context)

def crud(request):
    atenciones= Atencion.objects.all()
    context= {'atenciones': atenciones}
    return render(request, 'clientes/atenciones_list.html', context) 

def atencionesAdd(request):
    if request.method != "POST":
        mecanicos= Mecanico.objects.all()
        mantenciones= Mantencion.objects.all()
        context={'mecanicos':mecanicos,'mantenciones':mantenciones}
        return render(request, 'clientes/atenciones_add.html', context)
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
        return render(request, 'clientes/atenciones_add.html', context)


def atenciones_del(request,pk):
    context={}
    try:
        atencion=Atencion.objects.get(id_atencion=pk)

        atencion.delete()
        mensaje="Bien, datos eliminados..."
        atenciones= Atencion.objects.all()
        context= {'atenciones': atenciones, 'mensaje': mensaje}
        return render(request, 'clientes/atenciones_list.html', context)
    except:
        mensaje="Error, atencion no existe..."
        atenciones= Atencion.objects.all()
        context= {'atenciones': atenciones, 'mensaje': mensaje}
        return render(request, 'clientes/atenciones_list.html', context)

def atenciones_editFind(request,pk):
    if pk != "":
        atenciones= Atencion.objects.get(id_atencion=pk)
        mecanicos=Mecanico.objects.all()
        mantenciones= Mantencion.objects.all()

        context= {'atenciones': atenciones, 'mecanicos': mecanicos,'mantenciones': mantenciones}
        if atenciones:
            return render(request, 'clientes/atenciones_edit.html', context)
        else:
            context= {'mensaje': "Error, atencion no existe..."}
            return render(request, 'clientes/atenciones_list.html', context)

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
        return render(request, 'clientes/atenciones_edit.html',context)
    else:
        atenciones = Atencion.objects.all()
        context={'atenciones':atenciones}
        return render(request, 'clientes/atencion_list.html',context)
    
def crud_generos(request):
    generos = Genero.objects.all()
    context ={'generos':generos}
    print('enviando datos generos_list')
    return render(request,"clientes/generos_list.html",context)

def crud_atencion(request):
    atenciones= Atencion.objects.all()
    context= {'atenciones': atenciones}
    return render(request, 'clientes/atencion_list.html', context) 

def generosAdd(request):
    print("Estoy en generosAdd")
    context= {}

    if request.method == "POST":
        print("Es un post")
        form = GeneroForm(request.POST)
        if form.is_valid:
            print("Estoy en agregar")
            form.save()
            form=GeneroForm()
            context={'mensaje':"Ok, datos guardados",'form':form}
            return render(request,'clientes/generos_add.html', context)
    else:
        form = GeneroForm()
        context={'form':form}
        return render(request,'clientes/generos_add.html', context)

def atencionAdd(request):
    print("Estoy en atencionAdd")
    context= {}

    if request.method == "POST":
        print("Es un post")
        form = AtencionForm(request.POST)
        if form.is_valid:
            print("Estoy en agregar")
            form.save()
            form=AtencionForm()
            context={'mensaje':"Ok, datos guardados",'form':form}
            return render(request,'clientes/atencion_add.html', context)
    else:
        form = AtencionForm()
        context={'form':form}
        return render(request,'clientes/atencion_add.html', context)