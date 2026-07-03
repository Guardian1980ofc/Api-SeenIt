from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet, UserListViewSet, ListItemViewSet, ReviewViewSet, MovieSearchView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('lists', UserListViewSet)
router.register('items', ListItemViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = router.urls + [
    path('movies/search/', MovieSearchView.as_view(), name='movie-search'),
]