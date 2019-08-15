from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from random import randint
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image, AsyncImage
from kivy.properties import StringProperty

#class for the buttons - combines picture and behaviour of a button
class ImageButton(ButtonBehavior, AsyncImage):
    pass

#class for the different pictures in every level
class Picture(Widget):
    def __init__(self, index, word, source):
        #index of the picture for right positioning and checking the answer
        self.index = index
        #word which matches the picture
        self.word = word
        #the picture address
        self.source = source

class Level(Widget):
    def __init__(self, counter):
        #counter is the place where the score is kept
        self.counter = counter
        #the position of the picture with the right answer
        self.right_pos = randint(1, 4)
        #declaring the word for the label
        self.label_word = StringProperty()
        #questions is the database and questions_len is the count of the questions
        self.questions_len = 4
        #q_index randomly chooses index to get a question from the DB
        self.q_index = randint(0, self.questions_len - 1)
        #hardcored pictures
        self.icon1 = Picture(1, 'ball', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Basketball.jpeg/220px-Basketball.jpeg')
        self.icon2 = Picture(2, 'hat', 'https://d106cmemq27pil.cloudfront.net/media/catalog/product/cache/2/image/750x/040ec09b1e35df139433887a97daa66f/3/0/305-big-hat.jpg')
        self.icon3 = Picture(3, 'pizza', 'https://img.buzzfeed.com/thumbnailer-prod-us-east-1/dc23cd051d2249a5903d25faf8eeee4c/BFV36537_CC2017_2IngredintDough4Ways-FB.jpg')
        self.icon4 = Picture(4, 'fish', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdErPvLjaPgeZ-Kzo5tqATsgFq0qenb1d0bW7YUOsTiDpS1Nk0')
        #list of the pics
        self.icons = ['void', self.icon1, self.icon2, self.icon3, self.icon4]
        self.label_word = str(self.icons[self.right_pos].word)

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
            print(self.counter)

#class for the whole game
class Game(Widget):
    #current progress
    progress = 0
    #current level
    level = Level(progress)

    #resetiing score
    def score_reset(self):
        self.progress = 0
        new_level = Level(self.progress)
        self.level = new_level
        print("reset score")

    #check if the needed score is reached. If so - return true, else - false
    def win_check(self):
        if self.progress > 5:
            self.score_reset()
            return 1
        return 0

    #setting new level and conserving the current score
    def play(self):
        self.progress = self.level.counter
        new_level = Level(self.progress)
        self.level = new_level
        print('your progress is: ', self.progress)
        for i in range(1, 5):
            if self.level.right_pos == i:
                print('right answer is', self.level.icons[i].word)

#screen for the menu
class MenuScreen(Screen):
    pass
#screen for win
class WinScreen(Screen):
    pass
