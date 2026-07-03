from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response  
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from catalog.models import User, UserList, ListItem, Review
from catalog.services import TMDBService
from .serializer import UserSerializer, UserListSerializer, ListItemSerializer, ReviewSerializer
from .permissions import IsOwnerOrReadOnly
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserListViewSet(viewsets.ModelViewSet):
    queryset = UserList.objects.all().order_by('-created_at')
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all().order_by('-added_at')
    serializer_class = ListItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class MovieSearchView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Busca filmes no TMDB",
        description="Recebe um termo de busca e retorna os filmes correspondentes vindos da API do TMDB.",
        parameters=[
            OpenApiParameter(
                name='query',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                required=True,
                description='Nome ou termo de busca do filme (ex: Matrix)'
            )
        ],
        responses={200: dict}
    )
    def get(self, request):
        query = request.query_params.get('query', '')
        if not query:
            return Response({"error": "O parâmetro 'query' é obrigatório."}, status=400)
            
        data = TMDBService.search_movies(query=query)
        return Response(data)