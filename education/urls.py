from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'Lessons', views.LessonViewSet)
router.register(r'Comments', views.CommentViewSet)
router.register(r'votes', views.VoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
