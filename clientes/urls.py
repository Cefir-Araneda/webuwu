#from django.conf.urls import url
from django.urls import path 
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('crud', views.crud, name='crud'),
    path('atencionesAdd', views.atencionesAdd, name='atencionesAdd'),
    path('atenciones_del/<str:pk>', views.atenciones_del, name='atenciones_del'),
    path('atenciones_editFind/<str:pk>', views.atenciones_editFind, name='atenciones_editFind'),
    path('atencionesUpdate', views.atencionesUpdate, name='atencionesUpdate'),
]