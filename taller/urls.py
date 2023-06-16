#from django.conf.urls import url
from django.urls import path 
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('trabajosrecientes', views.trabajosrecientes, name = 'trabajosrecientes'),
    path('categoria', views.categoria, name = 'categoria'),
    path('mecanico', views.mecanico, name = 'mecanico'),
    path('contactanos', views.contactanos, name = 'contactanos'),
    path('signin', views.signin, name = 'signin'),
    path('signup', views.signup, name = 'signup'),

    path('trabajo1', views.trabajo1, name = 'trabajo1'),
    path('trabajo2', views.trabajo2, name = 'trabajo2'),
    path('trabajo3', views.trabajo3, name = 'trabajo3'),
    
    path('mantenciones', views.mantenciones, name = 'mantenciones'),
    path('notificaciones', views.notificaciones, name = 'notificaciones'),
    
    path('crud', views.crud, name='crud'),
    path('atencionesAdd', views.atencionesAdd, name='atencionesAdd'),
    path('atenciones_del/<str:pk>', views.atenciones_del, name='atenciones_del'),
    path('atenciones_editFind/<str:pk>', views.atenciones_editFind, name='atenciones_editFind'),
    path('atencionesUpdate', views.atencionesUpdate, name='atencionesUpdate'),
]