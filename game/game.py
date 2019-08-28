from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from random import randint
from classes import *

#loading kivy file
Builder.load_file('my.kv')

#class for the screen during the game
class GameScreen(Screen):
    #making new game
    game = Game()
    #new label setup
    def new_label(self, title):
        self.ids.label1.text = title\

    def btn_update(self, source):
        self.ids.btn1.source = source[0]
        self.ids.btn2.source = source[1]
        self.ids.btn3.source = source[2]
        self.ids.btn4.source = source[3]


    def build(self):
        return game().run()

#sm == Screen Manger
sm = ScreenManager()
sm.add_widget(MenuScreen(name = "menu"))
sm.add_widget(GameScreen(name = "game"))
sm.add_widget(WinScreen(name = "win_screen"))

sm.current = 'menu'

class MyApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    MyApp().run()
