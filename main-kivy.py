from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from functools import partial

class Container(FloatLayout):
    def remove_start_game_screen(self):
        self.ids.anch1.remove_widget(self.ids.bt1)
        self.ids.anch1.remove_widget(self.ids.anch2)

class MainApp(App):
    def build(self):
        anchor_main = AnchorLayout(anchor_x='center', anchor_y='center')
        self.b = Container()
        anchor_main.add_widget(self.b)
        return anchor_main

if __name__ == '__main__':
    MainApp().run()

