from django.urls import path
from . import views

urlpatterns=[
    path('meuscursos/', views.ListarCursosListView.as_view(),
         name='gerenciar_cursos_list'),
    path('', views.ListarCursosListView.as_view(),
         name='gerenciar_cursos_list'),
    path('criarcurso/', views.CriarCursoCreateView.as_view(),
         name='criar_curso'),
    path('editarcurso/<pk>/', views.AtualizarCursoUpdateView.as_view(),
         name='editar_curso'),
    path('excluircurso/<pk>/', views.ExcluirCursoDeleteView.as_view(),
         name='excluir_curso'),
    path('modulo/<pk>/', views.ModuloCursoUpdateView.as_view(),
         name='modulo_curso_update'),
    path('modulo/<int:modulo_id>/conteudo/<model_name>/criar/',
         views.CriarAtualizarConteudoView.as_view(),
         name='criar_conteudo_modulo'),
    path('modulo/<int:modulo_id>/conteudo/<model_name>/<id>/',
         views.CriarAtualizarConteudoView.as_view(),
         name='conteudo_modulo_update'),
    path('conteudo/excluir/<int:id_cont>/',
         views.ExcluirConteudoView.as_view(),
         name='excluir_conteudo_modulo'),
    path('modulo/<int:modulo_id>/conteudos',
         views.ListarConteudoModuloView.as_view(),
         name='listar_conteudo_modulo'),
]