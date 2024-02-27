from django.db import models

class Sede(models.Model):
    id_sede = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'api_sedes'

    def __str__(self):
        return f"{self.nombre}"

class Ventanilla(models.Model):
    id_ventanilla = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=20)
    nombres = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=50)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10)
    fecha = models.DateField()
    hora = models.CharField(max_length=5)
    detalles = models.TextField(null=True, blank=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField(default=1)
    asistencia = models.CharField(max_length=3, default='PE')
    id_abogado = models.IntegerField(null=True, blank=True)
    fecha_conf_coordinador = models.DateTimeField(null=True, blank=True)
    fecha_conf_abogado = models.DateTimeField(null=True, blank=True)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)

    class Meta:
        db_table = 'api_ventanilla'

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.nombres} - Sede { self.sede.nombre }"