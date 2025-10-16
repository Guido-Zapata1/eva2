from rest_framework import serializers
from .models import Especialidad, Medico, Paciente, ConsultaMedica, Tratamientos, Medicamento, RecetaMedica, HistorialAtencion, ExamenMedico

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMedica
        fields = '__all__'

class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamientos
        fields = '__all__'

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetaMedica
        fields = '__all__'

class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialAtencion
        fields = '__all__'

class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenMedico
        fields = '__all__'
