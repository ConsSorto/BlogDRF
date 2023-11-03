from rest_framework import serializers
from comments.models import Comment
from user.api.serializer import UserSerializer
from post.api.serializer import PostWithoutContentSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostWithoutContentSerializer()


    class Meta:
        model = Comment
        fields = ['content', 'created_at', 'user', 'post']