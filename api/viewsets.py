from rest_framework import viewsets
from .models import *
from .serializers import *

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaSerializer

class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamientos.objects.all()
    serializer_class = TratamientoSerializer

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaSerializer

class HistorialViewSet(viewsets.ModelViewSet):
    queryset = HistorialAtencion.objects.all()
    serializer_class = HistorialSerializer

class ExamenViewSet(viewsets.ModelViewSet):
    queryset = ExamenMedico.objects.all()
    serializer_class = ExamenSerializer
