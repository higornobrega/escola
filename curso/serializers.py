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
    
    # Relationship
    # 1. Nested Relationship:
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    
    # 2. HyperLinked Related Field:
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')
    
    # 3. Primary key Related Field:
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo', 
            'url', 
            'criacao', 
            'atualizacao', 
            'ativo',
            'avaliacoes'
        )