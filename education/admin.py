from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)


class LessonInline(admin.StackedInline):
    model = models.Lesson
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, ]
    list_display = ['id', 'name']
    list_filter = ['category']


class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'user', 'rating']
    list_filter = ['course', 'user']


admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Category)
admin.site.register(models.Lesson)
admin.site.register(models.Vote, VoteAdmin)
admin.site.register(models.Comment)
