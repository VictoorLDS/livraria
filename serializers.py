from rest_framework.serializers import ModelSerializers

from livraria.models import Categoria

class CategoriaSerializer (ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"