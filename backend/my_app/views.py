from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import StudentInfo, Question, Answer
from .serializers import StudentInfoSerializer, QuestionSerializer, AnswerSerializer


class StudentListAPIView(generics.ListCreateAPIView):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentInfoSerializer


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentInfoSerializer
    lookup_field = "student_chat_id"


class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
