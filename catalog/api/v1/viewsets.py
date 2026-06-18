from rest_framework import viewsets
from catalog.models import User, UserList, ListItem, Review
from .serializer import UserSerializer, UserListSerializer, ListItemSerializer, ReviewSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserListViewSet(viewsets.ModelViewSet):
    queryset = UserList.objects.all().order_by('-created_at')
    serializer_class = UserListSerializer


class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all().order_by('-added_at')
    serializer_class = ListItemSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer