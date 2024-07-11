from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .serializers import LikeSerializer, CommentSerializer, BlogSerializer
from .models import Like, Comment, Blog
from .permissions import BlogPermission, LikePermission, CommentPermission


class LikeAPIViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [LikePermission]


class BlogAPIViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [BlogPermission]


class CommentAPIViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]  