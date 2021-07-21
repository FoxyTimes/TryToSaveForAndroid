from kivy.app import App
from kivymd.app import MDApp
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
from kivy.uix.widget import Widget
from kivymd.uix.progressbar import MDProgressBar
from kivy.lang import Builder

runing = 0
temp = """
<Container>:
    AnchorLayout:
        id: anch1
        spacing: 20
        canvas:
            Rectangle:
                id: rec1
                source: 'img/darkPurple.png'
                size: self.size
                pos: self.pos
        Button:
            id: bt1
            size_hint: 0.19, 0.23
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            background_normal: 'img/button.png'
            background_down: 'img/button.png'
            on_press:
                root.remove_start_game_screen()
    AnchorLayout:
        id: anch2
        anchor_x: 'center'
        anchor_y: 'top'
        BoxLayout:
            id: box1
            orientation: 'vertical'
            size_hint: .4, .4
            Label:
                color: 1, 1, 0, 1
                text: 'TryToSave'
                font_size: 70
    AnchorLayout:
        id: anch3
        anchor_x: 'left'
        anchor_y: 'center'
    AnchorLayout:
        id: anch4
        anchor_x: 'right'
        anchor_y: 'center'
    AnchorLayout:
        id: anch5
        anchor_x: 'center'
        anchor_y: 'top'
        """


Builder.load_string(temp)


class Container(FloatLayout):
    def remove_start_game_screen(self):
        self.ids.anch1.remove_widget(self.ids.bt1)
        self.ids.anch2.remove_widget(self.ids.box1)
        self.money = 0
        self.start_game()
    def upgrade_1(self, instance):
        self.ids.anch5.remove_widget(self.lbl)
        self.plus += 1
        self.box = BoxLayout(orientation='vertical', size_hint=(1, .1))
        self.lbl = Label(text='Количество монет: ' + str(self.money) + '\nКоличество монет за клик: ' + str(self.plus), halign='center', valign='top', size_hint=(1, .2))
        self.ids.anch5.add_widget(self.lbl)
        self.damage_to_mob += 1
    def plus_money(self, instance):
        self.money += self.plus
        self.health -= self.damage_to_mob
        if self.health <= 0:
            self.health = 1000
            self.money += 1000
        self.ids.anch5.remove_widget(self.lbl)
        self.ids.anch4.remove_widget(self.box_with_mob)
        self.box_with_mob = BoxLayout(orientation='vertical', size_hint=(0.3, 0.7), padding=30)
        self.lbl = Label(text='Количество монет: ' + str(self.money) + '\nКоличество монет за клик: ' + str(self.plus), halign='center', valign='top', size_hint=(1, .2))
        self.lbl2 = MDProgressBar(max=1000, value=self.health, size_hint=(.5, .1), color=(1, 0, 0, 1), pos_hint={'center_x': .5, 'center_y': .5})
        self.ids.anch5.add_widget(self.lbl)
        self.box_with_mob.add_widget(self.lbl2)
        bt1 = (Button(background_normal='img/mob1.png', background_down='img/hit_mob1.png'))
        bt1.bind(on_release=self.plus_money)
        self.box_with_mob.add_widget(bt1)
        self.ids.anch4.add_widget(self.box_with_mob)
    def start_game(self):
        self.damage_to_mob = 1
        self.plus = 1
        self.health = 1000
        self.lbl = Label(text='Количество монет: ' + str(self.money) + '\nКоличество монет за клик: ' + str(self.plus), halign='center', valign='top', size_hint=(1, .2))
        self.box_with_upgrade = BoxLayout(orientation='vertical', padding=20, spacing=5, size_hint = (0.4, 0.2))
        self.box_with_mob = BoxLayout(orientation='vertical', size_hint=(0.7, 0.7), padding=30)
        bt1 = (Button(background_normal='img/mob1.png', background_down='img/hit_mob1.png'))
        bt2 = (Button(text='апгрейд 1', background_normal='img/btn1.png', font_size=10))
        bt3 = (Button(text='апгрейд 2', background_normal='img/btn1.png', font_size=10))
        bt1.bind(on_release=self.plus_money)
        bt2.bind(on_press=self.upgrade_1)
        self.lbl2 = MDProgressBar(max=1000, value=self.health, size_hint=(.5, .1), color=(1, 0, 0, 1), pos_hint={'center_x': .5, 'center_y': .5})
        self.box_with_mob.add_widget(self.lbl2)
        self.box_with_mob.add_widget(bt1)
        self.box_with_upgrade.add_widget(bt2)
        self.box_with_upgrade.add_widget(bt3)
        self.ids.anch5.add_widget(self.lbl)
        self.ids.anch3.add_widget(self.box_with_upgrade)
        self.ids.anch4.add_widget(self.box_with_mob)
class MainApp(MDApp):
    def build(self):
        self.b = Container()
        return self.b

if __name__ == '__main__':
    MainApp().run()

