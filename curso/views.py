# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Avaliacao, Curso
from .serializers import AvaliacaoSerializer, CursoSerialiser

# =================================== API V1 ===================================

class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerialiser
    
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerialiser
    
class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id = self.kwargs.get('curso_pk'))
        return self.queryset.all()
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))
    
# =================================== API V2 ===================================
    
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerialiser
    
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        
        # Pagination:
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id = pk)
        page = self.paginate_queryset(avaliacoes)
        
        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = AvaliacaoSerializer(avaliacoes.all(), many=True)
        return Response(serializer.data)
    
    

''' VIEWSET PADRÃO
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
'''

# VIEWSET CUSTOMIZADA (Retirado o 'mixins.ListModelMixin')
class AvaliacaoViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
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
