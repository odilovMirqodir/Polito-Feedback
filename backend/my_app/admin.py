from django.contrib import admin
from .models import StudentInfo, Question, Answer


@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = (
        "full_name", "course_name", "teacher_name", "language", "student_chat_id")
    search_fields = ("full_name", "course_name", "teacher_name")
    list_filter = ("course_name", "teacher_name")
    ordering = ("full_name",)
    readonly_fields = ("student_chat_id",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "question_text")
    search_fields = ("question_text",)
    ordering = ("id",)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("student", "question", "rating", "created_at")
    search_fields = ("student__full_name", "question__question_text")
    list_filter = ("rating", "created_at")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
