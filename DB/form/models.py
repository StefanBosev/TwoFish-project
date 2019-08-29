from django.db import models
import random

class Picture(models.Model):
    """
    class for the picture
    """
    word = models.CharField(max_length = 200)
    url = models.CharField(max_length = 500)

    @classmethod
    def get_four_random(cls):
        return Picture.objects.all().order_by('?')[:4]

class Question(models.Model):
    """
    class for the question
    """
    answer = models.ForeignKey(Picture, on_delete = None, blank = True, null = True)
    pics = models.ManyToManyField(Picture, blank = True, related_name = 'q_pics')

    def get_new(self):
        lst = list(Picture().get_four_random())
        self.answer = lst.pop(0)
        self.save()
        self.pics.set(lst)
        self.save()


class Answer(models.Model):
    """
    class for the answer
    """
    question = models.ForeignKey(Question, on_delete = None, blank = True, null = True, related_name = 'question_id')
    answer = models.ForeignKey(Picture, on_delete = None, blank = True, null = True, related_name = 'answer_id')

    def is_correct(self):
        return self.question.answer == self.answer
