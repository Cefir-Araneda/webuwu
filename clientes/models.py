from django.db import models

# Create your models here.

class Genero(models.Model):
  id_genero = models.AutoField(db_column='idGenero', primary_key=True)
  genero = models.CharField(max_length=20, blank=False, null=False) 

class Mecanico(models.Model):
    rut              = models.CharField(db_column='rut', primary_key=True,max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)

class Mantencion(models.Model):
    id_mantencion   = models.AutoField(primary_key=True,db_column='idMantencion')
    mantencion      = models.CharField(max_length=30, blank=False, null=False)

class Atencion(models.Model):
    id_atencion     = models.AutoField(primary_key=True, db_column='idAtencion')
    mecanico        = models.ForeignKey('Mecanico',on_delete=models.CASCADE, db_column='rut')
    fecha_atencion  = models.DateField(blank=False, null=False)
    modelo          = models.CharField(max_length=20)
    patente         = models.CharField(max_length=20)
    diagnostico     = models.CharField(max_length=100)
    id_mantencion   = models.ForeignKey('Mantencion', on_delete=models.CASCADE, db_column='idMantencion')
    cantidad        = models.CharField(max_length=20)
    valor           = models.CharField(max_length=20)