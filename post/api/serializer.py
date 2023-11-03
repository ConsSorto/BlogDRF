from rest_framework import serializers
from post.models import Post
from user.api.serializer import UserSerializer
from categories.api.serializer import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'miniature', 'created_at', 'user', 'category']


class PostWithoutContentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['title', 'slug', 'created_at', 'user', 'category']