# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import generics

from .models import Avaliacao, Curso
from .serializers import AvaliacaoSerializer, CursoSerialiser


class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerialiser
    
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerialiser
    
class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
# class CursoAPIView(APIView):
#     def get(self, request):
#         cursos = Curso.objects.all()
#         serializer = CursoSerialiser(cursos, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = CursoSerialiser(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # return Response({'msg': 'Criado com sucesso'}, status=status.HTTP_201_CREATED)
#         # return Response({'id': 'serializer.data['id'], 'curso':serializer.data['titulo']}, status=status.HTTP_201_CREATED)
    
# class AvaliacaoAPIView(APIView):
#     def get(self, request):
#         avaliacoes = Avaliacao.objects.all()
#         serialiser = AvaliacaoSerializer(avaliacoes, many=True)
#         return Response(serialiser.data)
    
#     def post(self, request):
#         serializer = AvaliacaoSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
