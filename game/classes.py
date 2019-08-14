from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder
from random import randint

class Level(Widget):
    def __init__(self, counter):
        self.counter = counter
        self.right_pos = randint(1, 4)
        self.questions = [['ball',
                        'image/ball.jpeg',
                        'image/partyhat.jpg',
                        'image/pizza.jpg',
                        'image/star.jpg'],
                    ['party hat',
                        'image/partyhat.jpg',
                        'image/ball.jpeg',
                        'image/pizza.jpg',
                        'image/star.jpg'],
                    ['pizza',
                        'image/pizza.jpg',
                        'image/star.jpg',
                        'image/ball.jpeg',
                        'image/partyhat.jpg'],
                    ['star',
                        'image/star.jpg',
                        'image/partyhat.jpg',
                        'image/ball.jpeg',
                        'image/pizza.jpg']
                    ]

        self.questions_len = len(self.questions)
        self.q_index = randint(0, self.questions_len - 1)

    def choice(self, name):
        if name == self.right_pos:
            return 1
        return 0


class MenuScreen(Screen):
    pass

class StudentScreen(Screen):
    pass

class TeacherScreen(Screen):
    pass

class GameScreen(Screen):
    def build(self):
        return main()

class WinScreen(Screen):
    pass
