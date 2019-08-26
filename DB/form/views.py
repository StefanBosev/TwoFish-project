from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from random import randint
from rest_framework import viewsets
from .serializers import QuestionSerializer, AnswerSerializer
from form.models import Question, Answer
import requests

#choosing random question from the all Questions D
def get_question():
    level = Question()
    level.get_new()
    return Question.objects.filter(id=level.id)

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    def get_queryset(self):
         return get_question()


#making new answer with the name of the question and the link from the chosen pic
# def set_question():
#     new_answer = requests.get('http://127.0.0.1:8000/question/set/?format=json')
#     new_answer.save()
#     return HttpResponse(new_answer)
#
# def check_answer(request, name, given_answer):
#     #getting question and it's answer
#     question = Question.objects.get(word=name)
#     answer = Answer.objects.get(index=name)
#
#     #if the right address equals the chosen by the kid - return true
#     if question.right_picture_address == answer.stud_answer:
#         answer.if_right = 1
#     else:
#         answer.if_right = 0
#     answer.save()
