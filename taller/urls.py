#from django.conf.urls import url
from django.urls import path 
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('trabajosrecientes', views.trabajosrecientes, name = 'trabajosrecientes'),
    path('categoria', views.categoria, name = 'categoria'),
    path('mecanico', views.mecanico, name = 'mecanico'),
    path('contactanos', views.contactanos, name = 'contactanos'),
    path('sign', views.sign, name = 'sign'),

    path('trabajo1', views.trabajo1, name = 'trabajo1'),
    path('trabajo2', views.trabajo2, name = 'trabajo2'),
    path('trabajo3', views.trabajo3, name = 'trabajo3'),
    
    path('agregar_atencion', views.agregar_atencion, name = 'agregar_atencion'),
    path('mantenciones', views.mantenciones, name = 'mantenciones'),
    path('notificaciones', views.notificaciones, name = 'notificaciones'),
    ]