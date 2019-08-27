from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from random import randint
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image, AsyncImage
from kivy.properties import StringProperty
import requests
import json

#class for the different pictures in every level
class Icon(Widget):
    def __init__(self, url, word):
        #picture word
        self.word = word
        #word which matches the picture
        self.url = url

class Level(Widget):
    def __init__(self, counter):
        #set dict
        self.question = requests.get('http://127.0.0.1:8000/question/get/').json()
        #counter is the place where the score is kept
        self.counter = counter
        #declaring the right position
        self.right_pos = randint(0, 3)
        #declaring the word for the label
        self.label_word = StringProperty()
        #icons list
        self.model = {Icon('', ''), Icon('', ''), Icon('', ''), Icon('', '')}
        self.icons = list(self.model)

        k = 0
        for i in range(0, len(self.icons)):
            if i == self.right_pos:
                self.icons[i].url = self.question['results'][0]['answer']['url']
                self.icons[i].word = self.question['results'][0]['answer']['word']
                continue
            self.icons[i].url = self.question['results'][0]['pics'][k]['url']
            self.icons[i].word = self.question['results'][0]['pics'][k]['word']
            k += 1

        #set label
        self.label_word = str(self.question['results'][0]['answer']['word'])

    #checking the given answer and changing the counter
    def choice(self, name):
        if name == self.right_pos:
            self.counter += 1
            return 1
        else:
            if self.counter <= 1:
                pass
            self.counter -= 1
        return 0

    #preventing the score from dropping under 0
    def score_check(self):
        if self.counter < 0:
            self.counter = 0

#class for the whole game
class Game(Widget):
    def __init__(self, **kwargs):
        #current progress
        self.progress = 0
        #current level
        self.level = Level(self.progress)

    #resetiing score
    def score_reset(self):
        self.progress = 0
        new_level = Level(self.progress)
        self.level = new_level
        print("reset score")
        print("\n")

    #check if the needed score is reached. If so - return true, else - false
    def win_check(self):
        if self.progress > 5:
            self.score_reset()
            return 1
        return 0

    # root.game.send_answer(self.name)
    def send_answer(self, given_answer):
        right_answer = self.level.question['results'][0]['answer']
        check = False

        if given_answer >= 3:
            post_data = {'right_answer': right_answer, 'stud_answer': self.level.question['results'][0]['pics'][given_answer - 1], 'if_right': check}
        else:
            post_data = {'right_answer': right_answer, 'stud_answer': self.level.question['results'][0]['pics'][given_answer], 'if_right': check}

        if right_answer['word'] == self.level.icons[given_answer].word:
            check = True
            post_data = {'right_answer': right_answer, 'stud_answer': right_answer, 'if_right': check}

        requests.post(url = 'http://127.0.0.1:8000/question/post', data = post_data)

    #setting new level and conserving the current score
    def play(self):
        self.progress = self.level.counter
        new_level = Level(self.progress)
        self.level = new_level
        print('your progress is: ', self.progress)

#screen for the menu
class MenuScreen(Screen):
    pass
#screen for win
class WinScreen(Screen):
    pass

#class for the buttons - combines picture and behaviour of a button
class ImageButton(ButtonBehavior, AsyncImage):
    pass
