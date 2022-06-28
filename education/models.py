from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Course(models.Model):
    name = models.CharField(max_length=50)
    # number_of_lessons
    create_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Vote(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField()

    class Meta:
        unique_together = ("user", "course")


class Lesson(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=500)
    detail = models.TextField()
    TYPE_CHOICES = [
        ('V', 'Video'),
        ('T', 'text'),
    ]
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
