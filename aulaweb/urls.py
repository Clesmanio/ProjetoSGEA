from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),

    path('cadastro', views.cadastro_usuario, name='cadastro_usuario'),
    path('login', views.login_usuario, name='login_usuario'),
    path('logout', views.logout_usuario, name='logout_usuario'),  
    path('eventos', views.list_eventos, name='list_eventos'), 
    path('eventos/<int:id>', views.detalhar_evento, name='detalhar_evento'), 
    path('eventos/novo', views.create_evento, name='create_evento'),
    path('eventos/editar/<int:id>', views.update_evento, name='update_evento'),
    path('eventos/remover/<int:id>', views.delete_evento, name='delete_evento'),
    path('minhas_inscricoes', views.list_inscricoes, name='list_inscricoes'),
    path('eventos/<int:evento_id>/inscrever', views.inscrever_evento, name='inscrever_evento'),
    path('inscricao/<int:inscricao_id>/certificado', views.emitir_certificado, name='emitir_certificado'),
    path('inscricao/cancelar/<int:inscricao_id>', views.cancelar_inscricao, name='cancelar_inscricao'),
]