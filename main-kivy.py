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
import random

runing = 0


class Container(FloatLayout):
    def remove_start_game_screen(self):
        self.ids.anch1.remove_widget(self.ids.bt1)
        self.ids.anch2.remove_widget(self.ids.box1)
        self.money = 0
        self.start_game()
    def upgrade_1(self, instance):
        self.ids.anch2.remove_widget(self.box)
        self.plus += 1
        self.box = BoxLayout(orientation='vertical')
        self.lbl = Label(text='Количество монет: ' + str(self.money) + '\nКоличество монет за клик: ' + str(self.plus), text_size=(self.width / 2, self.height - 100), halign='center', valign='top')
        self.box.add_widget(self.lbl)
        self.ids.anch2.add_widget(self.box)
        self.damage_to_mob += 1
    def plus_money(self, instance):
        self.ids.anch2.remove_widget(self.box)
        self.money += self.plus
        self.health -= self.damage_to_mob
        self.ids.anch4.remove_widget(self.box_with_mob)
        self.box_with_mob = BoxLayout(orientation='vertical', size_hint=(0.5, 0.7), padding=30)
        self.box = BoxLayout(orientation='vertical')
        self.lbl = Label(text='Количество монет: ' + str(self.money) + '\nКоличество монет за клик: ' + str(self.plus), text_size=(self.width / 2, self.height - 100), halign='center', valign='top')
        self.lbl2 = Label(text='Жизни врага: ' + str(self.health), halign='center', valign='top', size_hint=(1, .2))
        self.box.add_widget(self.lbl)
        self.ids.anch2.add_widget(self.box)
        self.box_with_mob.add_widget(self.lbl2)
        bt1 = (Button(text='клик'))
        bt1.bind(on_release=self.plus_money)
        self.box_with_mob.add_widget(bt1)
        self.ids.anch4.add_widget(self.box_with_mob)
    def start_game(self):
        self.damage_to_mob = 1
        self.plus = 1
        self.health = 1000
        self.box = BoxLayout(orientation='vertical')
        self.lbl = Label(text='Количество монет: ' + str(self.money) + '\nКоличество монет за клик: ' + str(self.plus), text_size=(self.width / 2, self.ids.anch1.height - 100), halign='center', valign='top')
        self.box.add_widget(self.lbl)
        self.ids.anch2.add_widget(self.box)
        self.box_with_upgrade = BoxLayout(orientation='vertical', padding=20, spacing=5, size_hint = (0.2, 0.2))
        self.box_with_mob = BoxLayout(orientation='vertical', size_hint=(0.5, 0.7), padding=30)
        bt1 = (Button(text='клик'))
        bt2 = (Button(text='апгрейд 1'))
        bt3 = (Button(text='апгрейд 2'))
        bt1.bind(on_release=self.plus_money)
        bt2.bind(on_press=self.upgrade_1)
        self.lbl2 = Label(text='Жизни врага: ' + str(self.health), halign='center', valign='top', size_hint=(1, .2))
        self.box_with_mob.add_widget(self.lbl2)
        self.box_with_mob.add_widget(bt1)
        self.box_with_upgrade.add_widget(bt2)
        self.box_with_upgrade.add_widget(bt3)
        self.ids.anch3.add_widget(self.box_with_upgrade)
        self.ids.anch4.add_widget(self.box_with_mob)
class MainApp(App):
    def build(self):
        self.b = Container()
        return self.b

if __name__ == '__main__':
    MainApp().run()


