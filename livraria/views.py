from rest_framework.viewsets import ModelViewSet

from livraria.models import Autor, Categoria, Editora, Livro
from livraria.serializers import AutorSerializer, CategoriaSerializer, EditoraSerializer, LivroSerializer, LivroDetailSerializer

from rest_framework.permissions import IsAuthenticated

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permissions_classes = [IsAuthenticated]

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LivroDetailSerializer
        return LivroSerializer
