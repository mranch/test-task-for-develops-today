from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'link']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
