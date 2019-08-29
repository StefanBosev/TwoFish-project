from form.models import Question, Picture, Answer
from rest_framework import serializers

class PictureSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Picture
        fields = ['pk',
                  'word',
                  'url'
                  ]

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answer = PictureSerializer()
    pics = PictureSerializer(many = True)
    class Meta:
        model = Question
        fields = ['pk',
                  'answer',
                  'pics'
                  ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'
