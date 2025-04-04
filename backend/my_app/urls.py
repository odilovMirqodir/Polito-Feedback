from django.urls import path
from .views import (
    StudentListAPIView, StudentRetrieveUpdateDestroyAPIView,
    QuestionListCreateAPIView, QuestionRetrieveUpdateDestroyAPIView,
    AnswerListCreateAPIView, AnswerRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path("students/", StudentListAPIView.as_view(), name="student-list"),
    path("students/<int:student_chat_id>/", StudentRetrieveUpdateDestroyAPIView.as_view(), name="student-detail"),

    path("questions/", QuestionListCreateAPIView.as_view(), name="question-list"),
    path("questions/<int:pk>/", QuestionRetrieveUpdateDestroyAPIView.as_view(), name="question-detail"),

    path("answers/", AnswerListCreateAPIView.as_view(), name="answer-list"),
    path("answers/<int:pk>/", AnswerRetrieveUpdateDestroyAPIView.as_view(), name="answer-detail"),
]
