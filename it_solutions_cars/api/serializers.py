from django.utils import timezone
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from cars.models import Car, Comment

class CarSerializer(serializers.ModelSerializer):

    owner = SlugRelatedField(slug_field='username', read_only=True)
    year = serializers.IntegerField(min_value=1885, required=False, max_value=timezone.now().year)

    class Meta:
        model = Car
        fields = '__all__'
        read_only_fields = ('owner', 'created_at', 'updated_at')

class CommentSerializer(serializers.ModelSerializer):

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'created_at', 'car')