from django.db import models

from pacientes.models import Paciente

# Create your models here.

class Cita(models.Model):  # las citas de guardan con relacio paciente-cita si no exite el paciente
    # se guardan sólo nombre apellidos correo telefono
    id_paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    fecha = models.DateField()
    hora = models.CharField(max_length=10)
    motivo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateField(auto_now_add=True)
    atendio = models.CharField(max_length=5)
    observacion = models.TextField(max_length=512)
    estatus = models.CharField(max_length=2)

    def _str__(self):
        return self.fecha

    class Meta:
        ordering = ['id']
