from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'taller/index.html', context)

def trabajosrecientes(request):
    context={}
    return render(request, 'taller/trabajosrecientes.html', context)

def categoria(request):
    context={}
    return render(request, 'taller/categoria.html', context)

def mecanico(request):
    context={}
    return render(request, 'taller/mecanico.html', context)

def contactanos(request):
    context={}
    return render(request, 'taller/contactanos.html', context)

def sign(request):
    context={}
    return render(request, 'taller/sign.html', context)

def trabajo1(request):
    context={}
    return render(request, 'taller/trabajo1.html', context)

def trabajo2(request):
    context={}
    return render(request, 'taller/trabajo2.html', context)

def trabajo3(request):
    context={}
    return render(request, 'taller/trabajo3.html', context)

def agregar_atencion(request):
    context={}
    return render(request, 'taller/agregar_atencion.html', context)

def mantenciones(request):
    context={}
    return render(request, 'taller/mantenciones.html', context)

def notificaciones(request):
    context={}
    return render(request, 'taller/notificaciones.html', context)

