from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

class Container(FloatLayout):
    pass

class Img(Image):
    pass


class Anch(AnchorLayout):
    pass

class MainApp(App):
    def build(self):
        anchor_main = AnchorLayout(anchor_x='center', anchor_y='center')
        b = Container()
        anchor_main.add_widget(b)
        anchor_main.add_widget(Anch())
        return anchor_main

if __name__ == '__main__':
    MainApp().run()