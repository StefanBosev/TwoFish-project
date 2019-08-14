from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, NumericProperty
from kivy.core.image import Image as CoreImage
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from random import randint

Builder.load_file('my.kv')

class MyGame(Widget):
    def __init__(self):
        self.counter = 0
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

    def r_count(self):
        self.counter += 1
        print(self.counter)

    def l_count(self):
        self.counter -= 1
        print(self.counter)

    def choice(self, name):
        if name == self.right_pos:
            self.r_count()
            print('right choice')
            #new_level = MyApp(self.counter)
        else:
            if self.counter < 1:
                print(self.counter)
            else:
                self.l_count()


class MenuScreen(Screen):
    pass

class StudentScreen(Screen):
    pass

class TeacherScreen(Screen):
    pass

class GameScreen(Screen):
    game = MyGame()
    def build(self):
        return game.run()

class WinScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name = "menu"))
sm.add_widget(StudentScreen(name = "stud_scr"))
sm.add_widget(TeacherScreen(name = "teach_scr"))
sm.add_widget(GameScreen(name = "game"))
sm.add_widget(WinScreen(name = "win_screen"))

sm.current = 'menu'


class MyApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    MyApp().run()
