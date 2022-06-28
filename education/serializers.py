from rest_framework import serializers
from . import models


class CurrentUserDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name']


class LessonOfCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = ['id', 'title', 'type']


class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=models.Category.objects.all(), source="category",
                                                     write_only=True)
    lessons = LessonOfCourseSerializer(read_only=True, many=True)
    number_of_lessons = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'create_date', 'category', 'number_of_lessons', 'category_id', 'lessons']

    def get_number_of_lessons(self, obj):
        return obj.lessons.count()


class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(queryset=models.Course.objects.all(), source="course",
                                                   write_only=True)
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        comments = obj.comments.all()
        return [{"user_name": i.user.username, "content": i.content} for i in comments]

    class Meta:
        model = models.Lesson
        fields = ['id', 'title', 'content', 'detail', 'type', 'course', 'course_id', 'comments']


class VoteSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(queryset=models.Course.objects.all(), source="course",
                                                   write_only=True)
    user_id = serializers.HiddenField(default=CurrentUserDefault(), source="user")
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.Vote
        fields = ['id', 'rating', 'course', 'course_id', 'user', 'user_id']


class CommentSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)
    lesson_id = serializers.PrimaryKeyRelatedField(queryset=models.Lesson.objects.all(), source="lesson",
                                                   write_only=True)
    user_id = serializers.HiddenField(default=CurrentUserDefault(), source="user")
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.Comment
        fields = ['id', 'content', 'lesson', 'lesson_id', 'user', 'user_id']
