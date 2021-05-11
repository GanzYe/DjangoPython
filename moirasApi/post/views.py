from django.contrib.auth.models import User
from .serializer import PostSerializer,ImagePostSerializer,UrlPostSerializer,CommentSerializer,UserSerializer
from .models import Post, ImagePost, UrlPost,Comment
from .myPagination import PostLimitOffsetPagination
from rest_framework import viewsets, permissions
from rest_framework import filters

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = PostLimitOffsetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class ImagePostViewSet(viewsets.ModelViewSet):
    serializer_class = ImagePostSerializer
    queryset = ImagePost.objects.all()
    pagination_class = PostLimitOffsetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UrlPostViewSet(viewsets.ModelViewSet):
    serializer_class = UrlPostSerializer
    queryset = UrlPost.objects.all()
    pagination_class = PostLimitOffsetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    pagination_class = PostLimitOffsetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]