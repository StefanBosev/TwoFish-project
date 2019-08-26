from django.urls import path, include

from .views import QuestionViewSet, AnswerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'get', QuestionViewSet, basename = 'question')
router.register(r'post', AnswerViewSet, basename = 'answer')

urlpatterns = [
    path('', include(router.urls)),
]
