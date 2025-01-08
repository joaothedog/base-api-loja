from django.urls import path, include
from . import views

urlpatterns = [
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produtos/criar/', views.criar_produto, name='criar_produto'),
    path('produtos/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('produtos/deletar/<int:id>/', views.deletar_produto, name='deletar_produto'),
]