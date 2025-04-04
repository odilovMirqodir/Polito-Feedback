from rest_framework import serializers
from .models import StudentInfo, Question, Answer


class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"




class AnswerSerializer(serializers.ModelSerializer):
    student_full_name = serializers.CharField(source="student.full_name", read_only=True)
    question_text = serializers.CharField(source="question.question_text", read_only=True)

    class Meta:
        model = Answer
        fields = ["id", "rating", "question", "student", "created_at", "updated_at", "student_full_name",
                  "question_text"]
        read_only_fields = ["created_at", "updated_at"]
