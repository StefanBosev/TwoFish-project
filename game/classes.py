from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from random import randint
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image, AsyncImage

class ImageButton(ButtonBehavior, AsyncImage):
    pass

class Picture(Widget):
    def __init__(self, index, word, source):
        self.index = index
        self.word = word
        self.source = source

class Level(Widget):
    def __init__(self, counter):
        self.counter = counter
        self.right_pos = randint(1, 4)
        self.questions_len = 4
        self.q_index = randint(0, self.questions_len - 1)
        self.icon1 = Picture(1, 'ball', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Basketball.jpeg/220px-Basketball.jpeg')
        self.icon2 = Picture(2, 'hat', 'https://d106cmemq27pil.cloudfront.net/media/catalog/product/cache/2/image/750x/040ec09b1e35df139433887a97daa66f/3/0/305-big-hat.jpg')
        self.icon3 = Picture(3, 'pizza', 'https://img.buzzfeed.com/thumbnailer-prod-us-east-1/dc23cd051d2249a5903d25faf8eeee4c/BFV36537_CC2017_2IngredintDough4Ways-FB.jpg')
        self.icon4 = Picture(4, 'fish', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdErPvLjaPgeZ-Kzo5tqATsgFq0qenb1d0bW7YUOsTiDpS1Nk0')
        self.icons = ['void', self.icon1, self.icon2, self.icon3, self.icon4]

    def choice(self, name):
        if name == self.right_pos:
            self.counter += 1
            return 1
        else:
            if self.counter <= 1:
                pass
            self.counter -= 1
        return 0

    def score_check(self):
        if self.counter < 0:
            self.counter = 0

class Game(BoxLayout):
    progress = 0
    level = Level(progress)

    def win_check(self):
        if self.progress > 5:
            return 1
        return 0

    def play(self):
        self.progress = self.level.counter
        new_level = Level(self.progress)
        self.level = new_level
        for i in range(1, 5):
            if self.level.right_pos == i:
                print('right answer is', self.level.icons[i].word)
        print('your progress is: ', self.progress)


class MenuScreen(Screen):
    pass

class WinScreen(Screen):
    pass
