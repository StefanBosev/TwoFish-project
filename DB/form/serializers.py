from form.models import Question, Picture, Answer
from rest_framework import serializers

class PictureSerializer(serializers.HyperlinkedModelSerializer):
    # word = serializers.CharField(max_length = 200)
    # url = serializers.CharField(max_length = 500)
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

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    question = PictureSerializer()
    answer = PictureSerializer()

    class Meta:
        model = Answer
        fields = '__all__'
