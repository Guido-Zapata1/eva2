from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import (
    Especialidad, Medico, Paciente, HistorialAtencion,
    ExamenMedico, Tratamientos, Medicamento, RecetaMedica
)
from django.urls import reverse_lazy
# ---------------------------------------------------------------------
# Vista de Inicio
# Página principal que muestra el landing page de la aplicación
# ---------------------------------------------------------------------
class HomeView(TemplateView):
    template_name = 'api/home.html'
# ---------------------------------------------------------------------
# Vistas CRUD para Especialidades
# Maneja el listado, creación, actualización y eliminación de especialidades médicas
# ---------------------------------------------------------------------
class EspecialidadListView(ListView):
    model = Especialidad
    template_name = 'api/especialidad/especialidad_list.html'
    context_object_name = 'especialidades'

class EspecialidadCreateView(CreateView):
    model = Especialidad
    fields = ['nombre', 'descripcion']
    template_name = 'api/especialidad/especialidad_form.html'
    success_url = '/especialidades/'

class EspecialidadUpdateView(UpdateView):
    model = Especialidad
    fields = ['nombre', 'descripcion']
    template_name = 'api/especialidad/especialidad_form.html'
    success_url = '/especialidades/'

class EspecialidadDeleteView(DeleteView):
    model = Especialidad
    template_name = 'api/especialidad/especialidad_confirm_delete.html'
    success_url = '/especialidades/'


# ---------------------------------------------------------------------
# Vistas CRUD para Pacientes
# Gestiona el registro, edición y eliminación de pacientes del sistema
# ---------------------------------------------------------------------
class PacienteListView(ListView):
    model = Paciente
    template_name = 'api/paciente/paciente_list.html'
    context_object_name = 'pacientes'

class PacienteCreateView(CreateView):
    model = Paciente
    fields = ['nombre', 'apellido', 'rut', 'fecha_nacimiento', 'telefono', 'direccion', 'tipo_sangre']
    template_name = 'api/paciente/paciente_form.html'
    success_url = '/pacientes/'

class PacienteUpdateView(UpdateView):
    model = Paciente
    fields = ['nombre', 'apellido', 'rut', 'fecha_nacimiento', 'telefono', 'direccion', 'tipo_sangre']
    template_name = 'api/paciente/paciente_form.html'
    success_url = '/pacientes/'

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'api/paciente/paciente_confirm_delete.html'
    success_url = '/pacientes/'


# ---------------------------------------------------------------------
# Vistas CRUD para Médicos
# Administra el registro, modificación y eliminación de médicos
# ---------------------------------------------------------------------
class MedicoListView(ListView):
    model = Medico
    template_name = 'api/medico/medico_list.html'
    context_object_name = 'medicos'

class MedicoCreateView(CreateView):
    model = Medico
    fields = ['nombre', 'apellido', 'rut', 'correo', 'telefono', 'especialidad', 'activo']
    template_name = 'api/medico/medico_form.html'
    success_url = '/medicos/'

class MedicoUpdateView(UpdateView):
    model = Medico
    fields = ['nombre', 'apellido', 'rut', 'correo', 'telefono', 'especialidad', 'activo']
    template_name = 'api/medico/medico_form.html'
    success_url = '/medicos/'

class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = 'api/medico/medico_confirm_delete.html'
    success_url = '/medicos/'


# ---------------------------------------------------------------------
# Vistas CRUD para Consultas Médicas / Historial de Atención
# Gestiona las consultas médicas realizadas a los pacientes
# ---------------------------------------------------------------------
class ConsultaListView(ListView):
    model = HistorialAtencion
    template_name = 'api/consulta/consulta_list.html'
    context_object_name = 'consultas'

class ConsultaCreateView(CreateView):
    model = HistorialAtencion
    fields = ['paciente', 'medico', 'diagnostico', 'observaciones']  # quitar 'fecha'
    template_name = 'api/consulta/consulta_form.html'
    success_url = '/consultas/'

class ConsultaUpdateView(UpdateView):
    model = HistorialAtencion
    fields = ['paciente', 'medico', 'fecha', 'diagnostico', 'observaciones']
    template_name = 'api/consulta/consulta_form.html'
    success_url = '/consultas/'

class ConsultaDeleteView(DeleteView):
    model = HistorialAtencion
    template_name = 'api/consulta/consulta_confirm_delete.html'
    success_url = '/consultas/'


# ---------------------------------------------------------------------
# Vistas CRUD para Historial Médico
# Maneja el historial completo de atención médica de los pacientes
# ---------------------------------------------------------------------
class HistorialListView(ListView):
    model = HistorialAtencion
    template_name = 'api/historiales/historial_list.html'
    context_object_name = 'historiales'

class HistorialCreateView(CreateView):
    model = HistorialAtencion
    fields = ['paciente', 'medico', 'diagnostico', 'tratamiento', 'observaciones']
    template_name = 'api/historiales/historial_form.html'
    success_url = reverse_lazy('historial_list')

class HistorialUpdateView(UpdateView):
    model = HistorialAtencion
    fields = ['paciente', 'medico', 'diagnostico', 'tratamiento', 'observaciones']
    template_name = 'api/historiales/historial_form.html'
    success_url = reverse_lazy('historial_list')

class HistorialDeleteView(DeleteView):
    model = HistorialAtencion
    template_name = 'api/historiales/historial_confirm_delete.html'
    success_url = reverse_lazy('historial_list')


# ---------------------------------------------------------------------
# Vistas CRUD para Exámenes Médicos
# Administra los exámenes médicos realizados a los pacientes
# ---------------------------------------------------------------------
class ExamenListView(ListView):
    model = ExamenMedico
    template_name = 'api/examenes/examen_list.html'
    context_object_name = 'examenes'

class ExamenCreateView(CreateView):
    model = ExamenMedico
    fields = ['historial', 'tipo_examen', 'resultado', 'fecha_examen', 'medico_responsable']
    template_name = 'api/examenes/examen_form.html'
    success_url = reverse_lazy('examen_list')

class ExamenUpdateView(UpdateView):
    model = ExamenMedico
    fields = ['historial', 'tipo_examen', 'resultado', 'fecha_examen', 'medico_responsable']
    template_name = 'api/examenes/examen_form.html'
    success_url = reverse_lazy('examen_list')

class ExamenDeleteView(DeleteView):
    model = ExamenMedico
    template_name = 'api/examenes/examen_confirm_delete.html'
    success_url = reverse_lazy('examen_list')


# ---------------------------------------------------------------------
# Vistas CRUD para Tratamientos
# Gestiona los tratamientos médicos prescritos a los pacientes
# ---------------------------------------------------------------------
class TratamientoListView(ListView):
    model = Tratamientos
    template_name = 'api/tratamientos/tratamiento_list.html'
    context_object_name = 'tratamientos'

class TratamientoCreateView(CreateView):
    model = Tratamientos
    fields = ['consulta', 'descripcion', 'duracion_dias', 'observaciones']
    template_name = 'api/tratamientos/tratamiento_form.html'
    success_url = '/tratamientos/'

class TratamientoUpdateView(UpdateView):
    model = Tratamientos
    fields = ['consulta', 'descripcion', 'duracion_dias', 'observaciones']
    template_name = 'api/tratamientos/tratamiento_form.html'
    success_url = '/tratamientos/'

class TratamientoDeleteView(DeleteView):
    model = Tratamientos
    template_name = 'api/tratamientos/tratamiento_confirm_delete.html'
    success_url = '/tratamientos/'


# ---------------------------------------------------------------------
# Vistas CRUD para Medicamentos
# Administra el inventario y registro de medicamentos disponibles
# ---------------------------------------------------------------------
class MedicamentoListView(ListView):
    model = Medicamento
    template_name = 'api/medicamentos/medicamento_list.html'
    context_object_name = 'medicamentos'

class MedicamentoCreateView(CreateView):
    model = Medicamento
    fields = ['nombre', 'laboratorio', 'stock', 'precio_unitario']
    template_name = 'api/medicamentos/medicamento_form.html'
    success_url = reverse_lazy('medicamento_list')

class MedicamentoUpdateView(UpdateView):
    model = Medicamento
    fields = ['nombre', 'laboratorio', 'stock', 'precio_unitario']
    template_name = 'api/medicamentos/medicamento_form.html'
    success_url = reverse_lazy('medicamento_list')

class MedicamentoDeleteView(DeleteView):
    model = Medicamento
    template_name = 'api/medicamentos/medicamento_confirm_delete.html'
    success_url = reverse_lazy('medicamento_list')


# ---------------------------------------------------------------------
# Vistas CRUD para Recetas Médicas
# Gestiona las recetas médicas emitidas para los tratamientos
# ---------------------------------------------------------------------
class RecetaMedicaListView(ListView):
    model = RecetaMedica
    template_name = 'api/recetas/receta_list.html'
    context_object_name = 'recetas'

class RecetaMedicaCreateView(CreateView):
    model = RecetaMedica
    fields = ['tratamiento', 'medicamento', 'dosis', 'frecuencia', 'duracion']
    template_name = 'api/recetas/receta_form.html'
    success_url = reverse_lazy('receta_list')

class RecetaMedicaUpdateView(UpdateView):
    model = RecetaMedica
    fields = ['tratamiento', 'medicamento', 'dosis', 'frecuencia', 'duracion']
    template_name = 'api/recetas/receta_form.html'
    success_url = reverse_lazy('receta_list')

class RecetaMedicaDeleteView(DeleteView):
    model = RecetaMedica
    template_name = 'api/recetas/receta_confirm_delete.html'
    success_url = reverse_lazy('receta_list')