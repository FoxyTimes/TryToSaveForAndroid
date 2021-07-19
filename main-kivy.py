from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from functools import partial
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
import time

runing = 0
class Container(FloatLayout):
    def remove_start_game_screen(self):
        self.ids.anch1.remove_widget(self.ids.bt1)
        self.ids.anch2.remove_widget(self.ids.box1)
        self.score = 0
        self.start_game()
    def start_game(self):
        self.box = BoxLayout(orientation='vertical')
        self.lbl = Label(text='Ваш счет: ' + str(self.score), text_size=(self.width / 2, self.height - 100), halign='center', valign='top')
        self.box.add_widget(self.lbl)
        self.ids.anch2.add_widget(self.box)
class MainApp(App):
    def build(self):
        self.b = Container()
        return self.b

if __name__ == '__main__':
    MainApp().run()


