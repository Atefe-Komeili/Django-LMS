import rest_framework
from . import models
from .serializers import CategorySerializer, CourseSerializer, LessonSerializer, CommentSerializer, VoteSerializer

from rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = models.Lesson.objects.all()
    serializer_class = LessonSerializer


class VoteViewSet(viewsets.ModelViewSet):
    permission_classes = [rest_framework.permissions.IsAuthenticatedOrReadOnly, ]
    queryset = models.Vote.objects.all()
    serializer_class = VoteSerializer


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [rest_framework.permissions.IsAuthenticatedOrReadOnly, ]
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializer
