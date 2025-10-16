from django.contrib import admin
from django.urls import path, include

from rest_framework import routers, permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .viewsets import (
    EspecialidadViewSet, MedicoViewSet, PacienteViewSet, ConsultaViewSet,
    TratamientoViewSet, MedicamentoViewSet, RecetaViewSet,
    HistorialViewSet, ExamenViewSet,
)

from .views import (
    HomeView,
    EspecialidadListView, EspecialidadCreateView, EspecialidadUpdateView, EspecialidadDeleteView,
    MedicoListView, MedicoCreateView, MedicoUpdateView, MedicoDeleteView,
    PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView,
    ConsultaListView, ConsultaCreateView, ConsultaUpdateView, ConsultaDeleteView,
    HistorialListView, HistorialCreateView, HistorialUpdateView, HistorialDeleteView,
    ExamenListView, ExamenCreateView, ExamenUpdateView, ExamenDeleteView,  # ← QUITA ExamenDetailView DE AQUÍ
    TratamientoListView, TratamientoCreateView, TratamientoUpdateView, TratamientoDeleteView,
    MedicamentoListView, MedicamentoCreateView, MedicamentoUpdateView, MedicamentoDeleteView,
    RecetaMedicaListView, RecetaMedicaCreateView, RecetaMedicaUpdateView, RecetaMedicaDeleteView,
)

# ---------------------------------------------------------------------
# Configuración del Router para API
# Registra todos los ViewSets para endpoints REST: Especialidad, Medico, Paciente,
# Consulta, Tratamiento, Medicamento, Receta, Historial y Examen
# ---------------------------------------------------------------------
router = routers.DefaultRouter()
router.register(r'especialidades', EspecialidadViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'consultas', ConsultaViewSet)
router.register(r'tratamientos', TratamientoViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'recetas', RecetaViewSet)
router.register(r'historiales', HistorialViewSet)
router.register(r'examenes', ExamenViewSet)

# ---------------------------------------------------------------------
# Configuración del Esquema Swagger
# Define metadatos (título, versión, descripción, contacto) y permite acceso público
# ---------------------------------------------------------------------
schema_view = get_schema_view(
    openapi.Info(
        title="API Clínica Salud Vital",
        default_version='v1',
        description="Documentación de la API de la clínica",
        contact=openapi.Contact(email="soporte@saludvital.cl"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # -----------------------------------------------------------------
    # Sitio de Administración de Django
    # -----------------------------------------------------------------
    path('admin/', admin.site.urls),

    # -----------------------------------------------------------------
    # Vista de Inicio (HomeView)
    # Página de destino única para usuarios autenticados o invitados
    # -----------------------------------------------------------------
    path('', HomeView.as_view(), name='home'),

    # -----------------------------------------------------------------
    # Vistas CRUD de Especialidad
    # Maneja listado, creación, actualización y eliminación de Especialidad
    # Clases: EspecialidadListView, EspecialidadCreateView,
    #          EspecialidadUpdateView, EspecialidadDeleteView
    # -----------------------------------------------------------------
    path('especialidades/',                      EspecialidadListView.as_view(),   name='especialidad_list'),
    path('especialidades/nueva/',                EspecialidadCreateView.as_view(), name='especialidad_create'),
    path('especialidades/<int:pk>/editar/',      EspecialidadUpdateView.as_view(), name='especialidad_update'),
    path('especialidades/<int:pk>/eliminar/',    EspecialidadDeleteView.as_view(), name='especialidad_delete'),

    # -----------------------------------------------------------------
    # Vistas CRUD de Médico
    # Clases: MedicoListView, MedicoCreateView,
    #          MedicoUpdateView, MedicoDeleteView
    # -----------------------------------------------------------------
    path('medicos/',                             MedicoListView.as_view(),         name='medico_list'),
    path('medicos/nuevo/',                       MedicoCreateView.as_view(),       name='medico_create'),
    path('medicos/<int:pk>/editar/',             MedicoUpdateView.as_view(),       name='medico_update'),
    path('medicos/<int:pk>/eliminar/',           MedicoDeleteView.as_view(),       name='medico_delete'),

    # -----------------------------------------------------------------
    # Vistas CRUD de Paciente
    # Clases: PacienteListView, PacienteCreateView,
    #          PacienteUpdateView, PacienteDeleteView
    # -----------------------------------------------------------------
    path('pacientes/',                           PacienteListView.as_view(),       name='paciente_list'),
    path('pacientes/nuevo/',                     PacienteCreateView.as_view(),     name='paciente_create'),
    path('pacientes/<int:pk>/editar/',           PacienteUpdateView.as_view(),     name='paciente_update'),
    path('pacientes/<int:pk>/eliminar/',         PacienteDeleteView.as_view(),     name='paciente_delete'),

    # -----------------------------------------------------------------
    # Vistas CRUD de Consulta
    # Clases: ConsultaListView, ConsultaCreateView,
    #          ConsultaUpdateView, ConsultaDeleteView
    # -----------------------------------------------------------------
    path('consultas/',                           ConsultaListView.as_view(),       name='consulta_list'),
    path('consultas/nueva/',                     ConsultaCreateView.as_view(),     name='consulta_create'),
    path('consultas/<int:pk>/editar/',           ConsultaUpdateView.as_view(),     name='consulta_update'),
    path('consultas/<int:pk>/eliminar/',         ConsultaDeleteView.as_view(),     name='consulta_delete'),

    # -----------------------------------------------------------------
    # Vistas CRUD de Historial
    # Clases: HistorialListView, HistorialCreateView,
    #          HistorialUpdateView, HistorialDeleteView
    # -----------------------------------------------------------------
    path('historiales/',                         HistorialListView.as_view(),      name='historial_list'),
    path('historiales/nuevo/',                   HistorialCreateView.as_view(),    name='historial_create'),
    path('historiales/<int:pk>/editar/',         HistorialUpdateView.as_view(),    name='historial_update'),
    path('historiales/<int:pk>/eliminar/',       HistorialDeleteView.as_view(),    name='historial_delete'),

    # -----------------------------------------------------------------
    # Vistas CRUD de Examen
    # Clases: ExamenListView, ExamenCreateView,
    #          ExamenUpdateView, ExamenDeleteView
    # -----------------------------------------------------------------
    path('examenes/',                            ExamenListView.as_view(),         name='examen_list'),
    path('examenes/nuevo/',                      ExamenCreateView.as_view(),       name='examen_create'),
    path('examenes/<int:pk>/editar/',            ExamenUpdateView.as_view(),       name='examen_update'),
    path('examenes/<int:pk>/eliminar/',          ExamenDeleteView.as_view(),       name='examen_delete'),
    # ELIMINA ESTA LÍNEA: path('examenes/<int:pk>/', ExamenDetailView.as_view(), name='examen_detail'),

    # -----------------------------------------------------------------
    # Vistas CRUD de Tratamiento
    # Clases: TratamientoListView, TratamientoCreateView,
    #          TratamientoUpdateView, TratamientoDeleteView
    # -----------------------------------------------------------------
    path('tratamientos/',                        TratamientoListView.as_view(),    name='tratamiento_list'),
    path('tratamientos/nuevo/',                  TratamientoCreateView.as_view(),  name='tratamiento_create'),
    path('tratamientos/<int:pk>/editar/',        TratamientoUpdateView.as_view(),  name='tratamiento_update'),
    path('tratamientos/<int:pk>/eliminar/',      TratamientoDeleteView.as_view(),  name='tratamiento_delete'),

    # -----------------------------------------------------------------
    # Vistas CRUD de Medicamento
    # Clases: MedicamentoListView, MedicamentoCreateView,
    #          MedicamentoUpdateView, MedicamentoDeleteView
    # -----------------------------------------------------------------
    path('medicamentos/',                        MedicamentoListView.as_view(),    name='medicamento_list'),
    path('medicamentos/nuevo/',                  MedicamentoCreateView.as_view(),  name='medicamento_create'),
    path('medicamentos/<int:pk>/editar/',        MedicamentoUpdateView.as_view(),  name='medicamento_update'),
    path('medicamentos/<int:pk>/eliminar/',      MedicamentoDeleteView.as_view(),  name='medicamento_delete'),

    # -----------------------------------------------------------------
    # Vistas CRUD de Receta Médica
    # Clases: RecetaMedicaListView, RecetaMedicaCreateView,
    #          RecetaMedicaUpdateView, RecetaMedicaDeleteView
    # -----------------------------------------------------------------
    path('recetas/',                             RecetaMedicaListView.as_view(),   name='receta_list'),
    path('recetas/nueva/',                       RecetaMedicaCreateView.as_view(), name='receta_create'),
    path('recetas/<int:pk>/editar/',             RecetaMedicaUpdateView.as_view(), name='receta_update'),
    path('recetas/<int:pk>/eliminar/',           RecetaMedicaDeleteView.as_view(), name='receta_delete'),

    # -----------------------------------------------------------------
    # Endpoints de API (ViewSets)
    # Montados bajo /api/ y proporcionan automáticamente listado, detalle,
    # creación, actualización y eliminación para todos los recursos registrados
    # -----------------------------------------------------------------
    path('api/', include(router.urls)),

    # -----------------------------------------------------------------
    # Interfaces de Documentación Swagger / Redoc
    # Documentación interactiva de API proporcionada por drf_yasg
    # -----------------------------------------------------------------
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/',   schema_view.with_ui('redoc', cache_timeout=0),   name='schema-redoc'),

    # -----------------------------------------------------------------
    # URLs de Autenticación
    # Login, logout y gestión de contraseñas proporcionados por Django
    # -----------------------------------------------------------------
    path('accounts/', include('django.contrib.auth.urls')),
]