from django.contrib import admin
from django.urls import path
from api.views import CancelarCitaView, SedeListCreate, SedeRetrieveUpdateDestroy, ConsultarVentanillaView, VentanillaListCreate, VentanillaRetrieveUpdateDestroy

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/sedes/', SedeListCreate.as_view(), name='sede-list-create'),
    path('api/sedes/<int:pk>/', SedeRetrieveUpdateDestroy.as_view(), name='sede-detail'),
    path('api/ventanillas/', VentanillaListCreate.as_view(), name='ventanilla-list-create'),
    path('api/ventanillas/<int:pk>/', VentanillaRetrieveUpdateDestroy.as_view(), name='ventanilla-detail'),

    path('api/ventanilla/consulta/<cedula>/', ConsultarVentanillaView.as_view(), name='consultar-ventanilla'),
    path('api/ventanilla/cancelar/<int:cita_id>/', CancelarCitaView.as_view(), name='cancelar_cita'),
]
