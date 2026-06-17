from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    profile_picture = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.username
    
class UserList(models.Model):
    LIST_TYPE_CHOICES = [
        ('movies', 'Movies Only'),
        ('tv', 'TV Shows Only'),
        ('anime', 'Anime Only'),
        ('all', 'Mixed/All'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    list_type = models.CharField(max_length=10, choices=LIST_TYPE_CHOICES, default='all')
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lists')

    def __str__(self):
        return f"{self.name} (by {self.user.username})"
    
class ListItem(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('movie', 'Movie'),
        ('tv', 'TV Show/Anime'),
    ]

    tmdb_id = models.IntegerField()
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    added_at = models.DateTimeField(auto_now_add=True)
    
    current_season = models.IntegerField(null=True, blank=True)
    current_episode = models.IntegerField(null=True, blank=True)

    list = models.ForeignKey(UserList, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f"{self.media_type.upper()} ID {self.tmdb_id} inside {self.list.name}"

class Review(models.Model):
    
    MEDIA_TYPE_CHOICES = [
        ('movie', 'Movie'),
        ('tv', 'TV Show/Anime'),
    ]

    tmdb_id = models.IntegerField()
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    rating = models.FloatField()
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        unique_together = ('user', 'tmdb_id', 'media_type')

    def __str__(self):
        return f"Review de {self.user.username} - Nota: {self.rating}"