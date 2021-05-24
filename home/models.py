from django.db import models

# Create your models here.
class Persona(models.Model):
        rut = models.CharField(max_length=12, null=False, blank=False, primary_key=True)
        nombre = models.CharField(max_length=100, null=False, blank=True)
        fechainicio = models.DateField(null=True)


class administrador(models.Model):
           rut_a= models.ForeignKey(Persona,null=False, on_delete=models.CASCADE)
           ct = [ ('1' , 'titular') , ('2' , 'asistente') ]
           cargo= models.CharField(max_length=15, null=False,blank=False,choices=ct)

class socio(models.Model):
           rut_s= models.ForeignKey(Persona, null=False, on_delete=models.CASCADE)
