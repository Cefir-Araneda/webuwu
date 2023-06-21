#from django.conf.urls import url
from django.urls import path 
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('index', views.index, name='index'),
    path('trabajosrecientes', views.trabajosrecientes, name = 'trabajosrecientes'),
    path('categoria', views.categoria, name = 'categoria'),
    path('mecanico', views.mecanico, name = 'mecanico'),
    path('galeria', views.galeria, name='galeria'),
    path('contactanos', views.contactanos, name = 'contactanos'),
    path('register', views.register, name = 'register'),

    path('trabajo1', views.trabajo1, name = 'trabajo1'),
    path('trabajo2', views.trabajo2, name = 'trabajo2'),
    path('trabajo3', views.trabajo3, name = 'trabajo3'),
    
    path('perfil', views.perfil, name = 'perfil'),
    path('mantenciones', views.mantenciones, name = 'mantenciones'),
    path('notificaciones', views.notificaciones, name = 'notificaciones'),
    
    path('crud', views.crud, name='crud'),
    path('atencionesAdd', views.atencionesAdd, name='atencionesAdd'),
    path('atenciones_del/<str:pk>', views.atenciones_del, name='atenciones_del'),
    path('atenciones_editFind/<str:pk>', views.atenciones_editFind, name='atenciones_editFind'),
    path('atencionesUpdate', views.atencionesUpdate, name='atencionesUpdate'),
]