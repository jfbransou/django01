from django.urls import path
from galeria.views import index, index2, imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
    path('index2', index2),
]
