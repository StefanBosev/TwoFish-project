from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from random import randint
from classes import *

Builder.load_file('my.kv')

sm = ScreenManager()
sm.add_widget(MenuScreen(name = "menu"))
sm.add_widget(GameScreen(name = "game"))
sm.add_widget(WinScreen(name = "win_screen"))

sm.current = 'menu'

def main():
    success_counter = 0

    while success_counter <= 5:
        level = Level(success_counter)


class MyApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    MyApp().run()
