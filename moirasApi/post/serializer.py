# from django.db.models import fields
from .models import Post,ImagePost,UrlPost,Comment
from rest_framework import serializers
from django.contrib.auth.models import User
# class TaskSerializer(serializers.Serializer):
    # description = serializers.CharField()
    # status = serializers.CharField()
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
class ImagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePost
        fields = '__all__'
class UrlPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlPost
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=['email'],
            username=validated_data['username']
        )
        user.is_active = True
        user.set_password(validated_data['password'])
        user.save()
        return user