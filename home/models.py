from django.db import models

# Create your models here.
class Persona(models.Model):
        rut = models.CharField(max_length=12, null=False, blank=False, primary_key=True)
        nombre = models.CharField(max_length=100, null=False, blank=True)
        fechainicio = models.DateField(null=True)
        ct = [('1', 'Directiva'), ('2', 'Socio')]
        cargo = models.CharField(max_length=15, null=False, blank=False, choices=ct)
        class meta:
            abstract=True


class administrador(models.Model):
    pass

class socio(models.Model):
    pass