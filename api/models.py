from django.db import models


# Opciones para tipo de sangre
TIPO_SANGRE_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

# Opciones para estado de la consulta
ESTADO_CONSULTA_CHOICES = [
    ('pendiente', 'Pendiente'),
    ('confirmada', 'Confirmada'),
    ('cancelada', 'Cancelada'),
]



class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    activo = models.BooleanField(default=True)
    especialidad = models.ForeignKey(
        Especialidad, on_delete=models.SET_NULL, null=True, related_name="medicos"
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Paciente(models.Model):
    rut = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    tipo_sangre = models.CharField(
        max_length=3,
        choices=TIPO_SANGRE_CHOICES,
        blank=True,
        null=True
    )
    correo = models.EmailField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class ConsultaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="consultas")
    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True, related_name="consultas")
    fecha_consulta = models.DateTimeField()
    motivo = models.TextField(blank=True, null=True)
    diagnostico = models.TextField(blank=True, null=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CONSULTA_CHOICES,
        default='pendiente'
    )

    def __str__(self):
        return f"Consulta {self.id} - {self.paciente}"


class Tratamientos(models.Model):
    consulta = models.ForeignKey(
        ConsultaMedica, on_delete=models.CASCADE, related_name="tratamientos"
    )
    descripcion = models.TextField()
    duracion_dias = models.PositiveIntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Tratamiento {self.id} - {self.consulta.paciente}"


class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100, blank=True, null=True)
    stock = models.IntegerField(default=0)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class RecetaMedica(models.Model):
    tratamiento = models.ForeignKey(
        Tratamientos, on_delete=models.CASCADE, related_name="recetas"
    )
    medicamento = models.ForeignKey(
        Medicamento, on_delete=models.CASCADE, related_name="recetas"
    )
    dosis = models.CharField(max_length=100, blank=True, null=True)
    frecuencia = models.CharField(max_length=100, blank=True, null=True)
    duracion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Receta {self.id} - {self.tratamiento.consulta.paciente}"

class HistorialAtencion(models.Model):
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='historiales')
    medico = models.ForeignKey('Medico', on_delete=models.SET_NULL, null=True, related_name='historiales')
    fecha = models.DateTimeField(auto_now_add=True)
    diagnostico = models.TextField()
    tratamiento = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Historial {self.id} - {self.paciente.nombre} {self.paciente.apellido}"

class ExamenMedico(models.Model):
    historial = models.ForeignKey(
        HistorialAtencion, 
        on_delete=models.CASCADE, 
        related_name='examenes',
        null=True  # <- permite valores nulos temporalmente
    )
    tipo_examen = models.CharField(max_length=100)
    resultado = models.TextField(blank=True, null=True)
    fecha_examen = models.DateField()
    medico_responsable = models.ForeignKey(
        'Medico', 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='examenes_realizados'
    )


    def __str__(self):
        return f"{self.tipo_examen} - {self.historial.paciente.nombre}"