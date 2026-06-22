from rest_framework import serializers
from catalog.models import User, UserList, ListItem, Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_picture', 'date_joined']
        read_only_fields = ['id', 'date_joined']


class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItem
        fields = ['id', 'list', 'tmdb_id', 'media_type', 'added_at', 'current_season', 'current_episode']
        read_only_fields = ['id', 'added_at']


class UserListSerializer(serializers.ModelSerializer):
    items = ListItemSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserList
        fields = ['id', 'name', 'description', 'list_type', 'is_public', 'created_at', 'user', 'items']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class ReviewSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'user_username', 'tmdb_id', 'media_type', 'rating', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_rating(self, value):
        if value < 0 or value > 10:
            raise serializers.ValidationError("A nota deve ser um valor entre 0.0 e 10.0.")
        return value

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)