from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

#def sign_in(request):

    #if request.method == 'GET':
     #   context={}
      #  return render(request, 'taller/signin.html', context)
    #else:
     #   if request.POST['password1'] == request.POST['password2']:
      #      User.objects.create_user(username = request.POST['username'])
       #     return HttpResponse('Las contraseñas no coinciden')


#def sign_up(request):
    #if request.method == 'GET':
     #   context={}
     #   return render(request, 'taller/signup.html', context)
    #else:
     #   if request.POST['password1'] == request.POST['password2']:
      #      User.objects.create_user(username = request.POST['username'])
       #     return HttpResponse('Las contraseñas no coinciden')

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

