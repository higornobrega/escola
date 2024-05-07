from rest_framework import serializers

from .models import Avaliacao, Curso


class AvaliacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        extra_kwargs = {
            'email' : {'write_only':True}
        }
        model= Avaliacao
        fields = (
            'id',
            'curso', 
            'nome', 
            'email', 
            'comentario', 
            'criacao', 
            'atualizacao', 
            'ativo'
        )
        
class CursoSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = (
            'titulo', 
            'url', 
            'criacao', 
            'atualizacao', 
            'ativo'
        )