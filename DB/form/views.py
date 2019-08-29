from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from random import randint
from rest_framework import viewsets
from .serializers import QuestionSerializer, AnswerSerializer
from form.models import Question, Answer
import requests
import ocean_motion

#choosing random question from the all Questions D
def get_question():
    level = Question()
    level.get_new()
    return Question.objects.filter(id=level.id)

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        serializer.save()
        if serializer.instance.is_correct():
            motor.up(10)
        else:
            motor.down(10)
        pass

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    def get_queryset(self):
        return get_question()
