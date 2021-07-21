from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

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
                pos: 0, self.height-45
            Rectangle:
                id: rec3
                source: 'img/bar_lvl.png'
                size: self.width/3, self.height/12
                pos: self.width/3, self.height-45
            Rectangle:
                id: rec4
                source: 'img/bar_mana.png'
                size: self.width/3, self.height/12
                pos: 2*(self.width/3), self.height-45
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
                pos: 10, self.height-35
            Rectangle:
                id: rec6
                source: 'img/lvl_icon.png'
                size: self.width/12, self.height/20
                pos: 10+self.width/3, self.height-35
            Rectangle:
                id: rec7
                source: 'img/mana_icon.png'
                size: self.width/12, self.height/20
                pos: 10+self.width/3+self.width/3, self.height-35
    BoxLayout:
        pos_hint: {'center_x': 0.5, 'center_y': 0.945}
        size_hint: 1, 1
        Label:
            color: 1, 1, 1, 1
            text: str(root.money)
            text_size: self.width/1.5, self.height/12
            font_size: 20
            halign: 'right'
            valign: 'top'
            size_hint: 1, 1
        Label:
            color: 1, 1, 1, 1
            text: str(root.lvl)
            text_size: self.width/1.5, self.height/12
            font_size: 20
            halign: 'right'
            valign: 'top'
            size_hint: 1, 1
        Label:
            color: 1, 1, 1, 1
            text: str(root.mana)
            text_size: self.width/1.5, self.height/12
            font_size: 20
            halign: 'right'
            valign: 'top'
            size_hint: 1, 1
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
            size_hint: 0.95, 0.5
            padding: 30
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
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
    health = ObjectProperty(1000)
    money = ObjectProperty(0)
    plus = ObjectProperty(1)
    damage = ObjectProperty(1)
    lvl = ObjectProperty(1)
    mana = ObjectProperty(10)
    def __init__(self, **kwargs):
        super(ScreenTwo, self).__init__(**kwargs)
    def plus_money(self):
        self.money += self.plus
    def plus_plus(self):
        self.plus += 1
    def minus_health(self):
        self.health -= self.damage

class ScreenThree(Screen):
    pass

class Manager(ScreenManager):

    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)

class ScreensApp(MDApp):
    def build(self):
        m = Manager(transition=NoTransition())
        return m

if __name__ == "__main__":
    ScreensApp().run()


