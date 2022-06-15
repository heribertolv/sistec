from django.urls import path

#Importar as Views Criadas
from .views import CampoCreate, AtividadeCreate

# Usar urlpatters por ser padrão do Django
urlpatterns = [
    path('cadastros/campo/', CampoCreate.as_view(), name="cadastrar-campo"),
    path('cadastros/atividade/', AtividadeCreate.as_view(), name="cadastrar-atividade"),
]