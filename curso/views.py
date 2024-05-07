from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Avaliacao, Curso
from .serializers import AvaliacaoSerializer, CursoSerialiser


class CursoAPIView(APIView):
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerialiser(cursos, many=True)
        return Response(serializer.data)
    
class AvaliacaoAPIView(APIView):
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serialiser = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serialiser.data)