from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from catalog.models import User, UserList, ListItem, Review
from .serializer import UserSerializer, UserListSerializer, ListItemSerializer, ReviewSerializer
from .permissions import IsOwnerOrReadOnly 

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
