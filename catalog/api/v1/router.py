from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet, UserListViewSet, ListItemViewSet, ReviewViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user')
router.register(r'lists', UserListViewSet, basename='userlist')
router.register(r'items', ListItemViewSet, basename='listitem')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]