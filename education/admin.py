from django.contrib import admin
from . import models


class LessonInline(admin.StackedInline):
    model = models.Lesson
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, ]
    list_display = ['id', 'name']
    list_filter = ['category']


admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Category)
admin.site.register(models.Lesson)
admin.site.register(models.Vote)
