from django.contrib import admin
from .models import Paciente, Medico, Especialidad, ConsultaMedica, Tratamientos, Medicamento, RecetaMedica,ExamenMedico,HistorialAtencion

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Especialidad)
admin.site.register(ConsultaMedica)
admin.site.register(Tratamientos)
admin.site.register(Medicamento)
admin.site.register(RecetaMedica)
admin.site.register(ExamenMedico)
admin.site.register(HistorialAtencion)