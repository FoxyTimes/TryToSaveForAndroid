from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition


def count(number):
    if number / 1000000000000000000000000000000 > 1.0:
        return str(number/1000000000000000000000000000000) + 'O'
    if number / 1000000000000000000000000000 > 1.0:
        return str(number/1000000000000000000000000000) + 'Sp'
    if number / 1000000000000000000000000 > 1.0:
        return str(number/1000000000000000000000000) + 'Sk'
    if number / 1000000000000000000000 > 1.0:
        return str(number/10000000000000000000000) + 'Qw'
    if number / 1000000000000000000 > 1.0:
        return str(number/11000000000000000000) + 'Qr'
    if number / 1000000000000000 > 1.0:
        return str(number/1000000000000000) + 'T'
    if number / 1000000000000 > 1.0:
        return str(number/1000000000000) + 'K'
    if number / 1000000000 > 1.0:
        return str(number/1000000000) + 'B'
    if number / 1000000 > 1.0:
        return str(number/1000000) + 'M'
    if number / 1000 > 1.0:
        return str(number/1000) + 'K'
    return str(number)

runing = 0
temp = """
<ScreenOne>:
    AnchorLayout:
        id: anch1
        spacing: 20
        canvas:
            Rectangle:
                id: rec1
                source: 'img/darkPurple.png'
                size: self.size
                pos: self.pos
    FloatLayout:
        id: fl1
        Button:
            id: bt1
            size_hint: 0.7, 0.23
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            background_normal: 'img/button.png'
            background_down: 'img/button.png'
            on_press:
                root.manager.current = "screen2"
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

<ScreenTwo>:
    AnchorLayout:
        id: anch1
        canvas:
            Rectangle:
                id: rec1
                source: 'img/darkPurple.png'
                size: self.size
                pos: self.pos
            Rectangle:
                id: rec2
                source: 'img/bar_money.png'
                size: self.width/3, self.height/12
                pos: 0, self.height-55
            Rectangle:
                id: rec3
                source: 'img/bar_lvl.png'
                size: self.width/3, self.height/12
                pos: self.width/3, self.height-55
            Rectangle:
                id: rec4
                source: 'img/bar_mana.png'
                size: self.width/3, self.height/12
                pos: 2*(self.width/3), self.height-55
    FloatLayout:
        id: fl1
        Button:
            id: bt1
            text: 'Меню'
            size_hint: 0.3, 0.1
            pos_hint: {'center_x': 0.15, 'center_y': 0.88}
            background_normal: 'img/btn1.png'
            background_down: 'img/btn1.png'
            on_press:
                root.manager.current = "screen1"
    AnchorLayout:
        id: anch1
        canvas:
            Rectangle:
                id: rec5
                source: 'img/money_icon.png'
                size: self.width/12, self.height/20
                pos: 10, self.height-45
            Rectangle:
                id: rec6
                source: 'img/lvl_icon.png'
                size: self.width/12, self.height/20
                pos: 10+self.width/3, self.height-45
            Rectangle:
                id: rec7
                source: 'img/mana_icon.png'
                size: self.width/12, self.height/20
                pos: 10+self.width/3+self.width/3, self.height-45
    BoxLayout:
        pos_hint: {'center_x': 0.5, 'center_y': 0.93}
        size_hint: 1, 1
        MDLabel:
            color: 1, 1, 1, 1
            text: str(root.return_money)
            text_size: self.width/1.5, self.height/12
            font_size: 20
            halign: 'right'
            valign: 'top'
            size_hint: 1, 1
            font_style: 'H6'
        MDLabel:
            color: 1, 1, 1, 1
            text: str(app.return_damage)
            text_size: self.width/1.5, self.height/12
            font_size: 20
            halign: 'right'
            valign: 'top'
            size_hint: 1, 1
            font_style: 'H6'
        MDLabel:
            color: 1, 1, 1, 1
            text: str(root.return_mana)
            text_size: self.width/1.5, self.height/12
            font_size: 20
            halign: 'right'
            valign: 'top'
            size_hint: 1, 1
            font_style: 'H6'
    FloatLayout:
        id: fl3
        BoxLayout:
            orientation: 'vertical'
            padding: 20
            spacing: 5
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            size_hint: 0.6, 0.2
            Button:
                text: 'Улучшения'
                background_normal: 'img/btn1.png'
                font_size: 25
                on_press: root.manager.current = "screen3"
    FloatLayout:
        id: fl4
        BoxLayout:
            orientation: 'vertical'
            size_hint: 0.95, 0.7
            padding: 30
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                halign: 'center'
                font_style: 'H6'
                text: str(root.return_health) + ' HP'
                color: 1, 0, 0, 1
                size_hint: 0.5, 0.1
                font_size: 20
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            MDProgressBar:
                max: 1000
                value: root.health
                size_hint: 0.5, 0.01
                color: 1, 0, 0, 1
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                
            Button:
                background_normal: 'img/mob1.png'
                background_down: 'img/hit_mob1.png'
                size_hint: 1, 1
                on_release: root.plus_money(), root.minus_health()

<ScreenThree>:
    FloatLayout:
        BoxLayout:
            spacing: 20
            pos_hint: {'center_x': 0.5, 'center_y': 0.95}
            size_hint: .9, .07
            Button:
                text: 'улучшения'
            Button:
                text: 'скилы'
            Button:
                text: 'в разработке'
        ScrollView:
            size_hint_y: .8
            do_scroll_x: False
            do_scroll_y: True
            pos_hint: {'x':0.25, 'y': .05}
            GridLayout:
                size:(root.width/2, root.height/4)
                size_hint_x: None
                size_hint_y: None
                spacing: 20
                cols: 1
                height: self.minimum_height
                Button:
                    size_hint: 1, 0.4
                    text: 'Увеличить количество пушек   ' + str(root.guns1)
                    on_press: root.up_guns1()
                Button:
                    size_hint: 1, 0.4
                    text: 'Улучшение 2'
                Button:
                    size_hint: 1, 0.4
                    text: 'Улучшение 3'
        BoxLayout:
            spacing: 20
            pos_hint: {'center_x': 0.8, 'center_y': 0.1}
            size_hint: .2, .07
            Button:
                text: 'назад'
                on_press:
                    root.manager.current = "screen2"
            
    
                
<Manager>:
    id: screen_manager
    screen_one: screen_one
    screen_two: screen_two
    screen_three: screen_three
    ScreenOne:
        id: screen_one
        name: "screen1"
        manager: screen_manager
    ScreenTwo:
        id: screen_two
        name: "screen2"
        manager: screen_manager
    ScreenThree:
        id: screen_three
        name: "screen3"
        manager: screen_manager
        """

Builder.load_string(temp)


class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    return_health = StringProperty('1000')
    return_money = StringProperty('0')
    plus = ObjectProperty(1)
    lvl = ObjectProperty(1)
    return_mana = StringProperty('10')
    def __init__(self, **kwargs):
        super(ScreenTwo, self).__init__(**kwargs)
        self.damage = App.get_running_app().damage
        self.health = 1000
        self.money = 0
        self.mana = 10
        self.return_mana = count(self.mana)
    def plus_money(self):
        self.money += self.plus
        self.return_money = count(self.money)
        print(count(self.money), count(self.mana), count(self.damage))
    def plus_plus(self):
        self.plus += 1
    def minus_health(self):
        self.health -= self.get_damage()
        self.return_health = count(self.health)
        if self.health <= 0:
            self.health = 1000
            self.money += 1000
    def get_damage(self):
        return App.get_running_app().damage

class ScreenThree(Screen):
    guns1 = ObjectProperty(1)
    def __init__(self, **kwargs):
        super(ScreenThree, self).__init__(**kwargs)
    def up_guns1(self):
        self.guns1 += 1
        App.get_running_app().damage += 1
        App.get_running_app().return_damage = count(App.get_running_app().damage)
class Manager(ScreenManager):

    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)

class ScreensApp(MDApp):
    damage = ObjectProperty(1)
    return_damage = StringProperty('1')
    def build(self):
        m = Manager(transition=NoTransition())
        return m

if __name__ == "__main__":
    ScreensApp().run()


