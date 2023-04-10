from django.urls import path
from .views import Registro, cerrarSession, logear

urlpatterns = [
    path('', Registro.as_view(), name="login"),
    path('cerrarSession', cerrarSession, name="cerrarSession"),
    path('logear', logear, name="logear"),
]

