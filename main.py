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
            size_hint: 0.19, 0.23
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
        spacing: 20
        canvas:
            Rectangle:
                id: rec1
                source: 'img/darkPurple.png'
                size: self.size
                pos: self.pos
    FloatLayout:
        id: fl2
        BoxLayout:
            orientation: 'vertical'
            padding: 20
            spacing: 5
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            size_hint: 0.6, 0.2
            Button:
                text: 'Улучшения'
                background_normal: 'img/btn1.png'
                font_size: 10
                on_press: root.manager.current = "screen3"
    FloatLayout:
        id: fl3
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
    AnchorLayout:
        id: anch5
        anchor_x: 'center'
        anchor_y: 'top'
        Label:
            text: 'Количество монет: ' + str(root.money)
            halign: 'center'
            valign: 'top'
            size_hint: 1, 0.2
        Label:
            text: 'Количество монет за клик: ' + str(root.plus)
            halign: 'center'
            valign: 'top'
            size_hint: 1, 0.25

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


