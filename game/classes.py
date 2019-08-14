from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder
from random import randint

class Level(Widget):
    def __init__(self, counter):
        self.counter = counter
        self.right_pos = randint(1, 4)
        self.questions_len = 4
        self.q_index = randint(0, self.questions_len - 1)

    def choice(self, name):
        if name == self.right_pos:
            self.counter += 1
            print(self.counter)
            return 1
        else:
            if self.counter <= 1:
                pass
            self.counter -= 1
        return 0

    def score_check(self):
        if self.counter < 0:
            self.counter = 0
            print(self.counter)

class Game(Widget):
    progress = 0
    level = Level(progress)

    def win_check(self):
        if self.progress > 5:
            print('you win')

    def play(self):
        self.progress = self.level.counter
        new_level = Level(self.progress)
        self.level = new_level
        print('your progress is: ', self.progress)

    def build(self):
        start = Main()

class MenuScreen(Screen):
    pass

class WinScreen(Screen):
    pass
