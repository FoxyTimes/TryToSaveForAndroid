from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition


def count(number):
    if number / 1000000000000000000000000000000 > 1.0:
        return str("%.1f" % (number/1000000000000000000000000000000)) + 'O'
    if number / 1000000000000000000000000000 > 1.0:
        return str("%.1f" % (number/1000000000000000000000000000)) + 'Sp'
    if number / 1000000000000000000000000 > 1.0:
        return str("%.1f" % (number/1000000000000000000000000)) + 'Sk'
    if number / 1000000000000000000000 > 1.0:
        return str("%.1f" % (number/10000000000000000000000)) + 'Qw'
    if number / 1000000000000000000 > 1.0:
        return str("%.1f" % (number/11000000000000000000)) + 'Qr'
    if number / 1000000000000000 > 1.0:
        return str("%.1f" % (number/1000000000000000)) + 'T'
    if number / 1000000000000 > 1.0:
        return str("%.1f" % (number/1000000000000)) + 'K'
    if number / 1000000000 > 1.0:
        return str("%.1f" % (number/1000000000)) + 'B'
    if number / 1000000 > 1.0:
        return str("%.1f" % (number/1000000)) + 'M'
    if number / 1000 > 1.0:
        return str("%.1f" % (number/1000)) + 'K'
    return str(int(number))

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
    FloatLayout:
        canvas:
            Rectangle:
                id: rec2
                source: 'img/bar_money.png'
                size: self.width/3, self.height/12
                pos: 0, self.height-self.height/2/2/2/1.5
            Rectangle:
                id: rec3
                source: 'img/bar_lvl.png'
                size: self.width/3, self.height/12
                pos: self.width/3, self.height-self.height/2/2/2/1.5
            Rectangle:
                id: rec4
                source: 'img/bar_mana.png'
                size: self.width/3, self.height/12
                pos: 2*(self.width/3), self.height-self.height/2/2/2/1.5
            Rectangle:
                id: rec5
                source: 'img/money_icon.png'
                size: root.width/12, root.height/20
                pos: 10, self.height-self.height/2/2/2/2
            Rectangle:
                id: rec6
                source: 'img/lvl_icon.png'
                size: root.width/12, root.height/20
                pos: 10+root.width/3, self.height-self.height/2/2/2/2
            Rectangle:
                id: rec7
                source: 'img/mana_icon.png'
                size: root.width/12, root.height/20
                pos: 10+root.width/3+root.width/3, self.height-self.height/2/2/2/1.8
    FloatLayout:
        BoxLayout:
            pos: self.width/16, self.height/3+self.height/2/2/1.65
            size_hint: 1, 1
            MDLabel:
                color: 1, 1, 1, 1
                text: str(app.return_money)
                text_size: self.width/1.5, self.height/12
                font_size: 20
                size_hint: 1, 1
                font_style: 'H6'
            MDLabel:
                color: 1, 1, 1, 1
                text: str(app.return_damage)
                text_size: self.width/1.5, self.height/12
                font_size: 20
                size_hint: 1, 1
                font_style: 'H6'
            MDLabel:
                color: 1, 1, 1, 1
                text: str(root.return_mana)
                text_size: self.width/1.5, self.height/12
                font_size: 20
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
                max: 300
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
        canvas:
            Rectangle:
                id: rec1
                source: 'img/darkPurple.png'
                size: self.size
                pos: self.pos
        BoxLayout:
            pos_hint: {'center_x': 0.5, 'center_y': 0.9}
            size_hint: 1, .09
            Button:
                text: 'урон'
                background_normal: 'img/btn1.png'
                background_down: 'img/btn1.png'
                size_hint: 1, 1.7
                font_size: 15
            Button:
                text: 'способности'
                background_normal: 'img/btn1.png'
                background_down: 'img/btn1.png'
                size_hint: 1.5, 1.7
                font_size: 15
            Button:
                text: 'деньги'
                background_normal: 'img/btn1.png'
                background_down: 'img/btn1.png'
                size_hint: 1, 1.7
                font_size: 15
        ScrollView:
            size_hint_y: 0.8
            do_scroll_x: False
            do_scroll_y: True
            pos_hint: {'x':0.025, 'y': .05}
            GridLayout:
                size:(root.width/2+root.width/2/2+root.width/2/2/1.25, root.height/4)
                size_hint_x: None
                size_hint_y: None
                spacing: 20
                cols: 1
                height: self.minimum_height
                canvas:
                    Rectangle:
                        id: rec1
                        source: 'img/background.jpg'
                        size: self.size
                        pos: self.pos
                FloatLayout:
                    canvas:
                        Rectangle:
                            id: rec1
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/2, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            id: rec1
                            source: 'img/fon.jpg'
                            size: self.size[0]/5, self.size[1]/1.5
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            id: rec1
                            source: 'img/upgrade1.png'
                            size: self.size[0]/5.5, self.size[1]/2
                            pos: self.pos[0]+10, self.pos[1]+10
                        Rectangle:
                            id: rec1
                            source: 'img/page1.png'
                            size: self.size[0]/3.5, self.size[1]+self.height/2/2/1.5
                            pos: self.pos[0]-self.width/2/2/2/2/3, self.pos[1]-self.height/2/2/2
                    BoxLayout:
                        size_hint: 1, 1
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_guns1)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Плазмопушка'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        id: d1
                        size_hint: 0.5, 1.7
                        pos_hint: {'center_x': 0.75, 'center_y': 0.45}
                        text: str(root.return_price1)
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1.png'
                        font_size: 15
                        on_press: root.up_guns1()
                FloatLayout:
                    canvas:
                        Rectangle:
                            id: rec1
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/2, self.size[1]+self.height/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            id: rec1
                            source: 'img/fon.jpg'
                            size: self.size[0]/5, self.size[1]/1.5
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            id: rec1
                            source: 'img/upgrade2.png'
                            size: self.size[0]/5.5, self.size[1]/2
                            pos: self.pos[0]+10, self.pos[1]+10
                        Rectangle:
                            id: rec1
                            source: 'img/page1.png'
                            size: self.size[0]/3.5, self.size[1]+self.height/2/2/1.5
                            pos: self.pos[0]-self.width/2/2/2/2/3, self.pos[1]-self.height/2/2/2
                    BoxLayout:
                        size_hint: 1, 1
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_guns2)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Лазер'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        id: d1
                        size_hint: 0.5, 1.7
                        pos_hint: {'center_x': 0.75, 'center_y': 0.45}
                        text: str(root.return_price2)
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1.png'
                        font_size: 15
                        on_press: root.up_guns2()
                FloatLayout:
                    canvas:
                        Rectangle:
                            id: rec1
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/2, self.size[1]+self.height/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            id: rec1
                            source: 'img/fon.jpg'
                            size: self.size[0]/5, self.size[1]/1.5
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            id: rec1
                            source: 'img/upgrade3.png'
                            size: self.size[0]/5.5, self.size[1]/2
                            pos: self.pos[0]+10, self.pos[1]+10
                        Rectangle:
                            id: rec1
                            source: 'img/page1.png'
                            size: self.size[0]/3.5, self.size[1]+self.height/2/2/1.5
                            pos: self.pos[0]-self.width/2/2/2/2/3, self.pos[1]-self.height/2/2/2
                    BoxLayout:
                        size_hint: 1, 1
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_guns3)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Ракета'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        id: d1
                        size_hint: 0.5, 1.7
                        pos_hint: {'center_x': 0.75, 'center_y': 0.45}
                        text: str(root.return_price3)
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1.png'
                        font_size: 15
                        on_press: root.up_guns3()
        BoxLayout:
            spacing: 20
            pos_hint: {'center_x': 0.8, 'center_y': 0.1}
            size_hint: .25, .15
            Button:
                text: 'назад'
                background_normal: 'img/btn1.png'
                background_down: 'img/btn1.png'
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
    return_health = StringProperty('300')
    return_money = StringProperty('0')
    plus = ObjectProperty(1)
    lvl = ObjectProperty(1)
    return_mana = StringProperty('10')
    health = ObjectProperty(300)
    def __init__(self, **kwargs):
        super(ScreenTwo, self).__init__(**kwargs)
        self.damage = App.get_running_app().damage
        self.health = 300
        self.money = App.get_running_app().money
        self.mana = 10
        self.return_mana = count(self.mana)
    def plus_money(self):
        self.money = App.get_running_app().money
        self.money += self.plus
        App.get_running_app().money = self.money
        App.get_running_app().return_money = count(self.money)
    def plus_plus(self):
        self.plus += 1
    def minus_health(self):
        check = self.health - self.get_damage()
        if check <= 0:
            self.health = 300 + self.get_damage()
            App.get_running_app().money += 100
        self.health -= self.get_damage()
        self.return_health = count(self.health)
        App.get_running_app().return_money = count(App.get_running_app().money)
    def get_damage(self):
        return App.get_running_app().damage

class ScreenThree(Screen):
    return_guns1 = StringProperty('1')
    return_guns2 = StringProperty('0')
    return_guns3 = StringProperty('0')
    return_price1 = StringProperty('100')
    return_price2 = StringProperty('1.0K')
    return_price3 = StringProperty('10.0K')
    def __init__(self, **kwargs):
        super(ScreenThree, self).__init__(**kwargs)
        self.guns1 = 1
        self.guns2 = 0
        self.guns3 = 0
        self.price1 = 100
        self.price2 = 1000
        self.price3 = 10000
        self.money = App.get_running_app().money
    def up_guns1(self):
        self.money = App.get_running_app().money
        if self.money > self.price1:
            self.guns1 += 1
            App.get_running_app().damage += 1
            App.get_running_app().return_damage = count(App.get_running_app().damage)
            self.return_guns1 = count(self.guns1)
            self.money -= self.price1
            App.get_running_app().money -= self.price1
            self.price1 *= 1.1
            self.price1 = int(self.price1)
            App.get_running_app().return_money = count(self.money)
            self.return_price1 = count(self.price1)
    def up_guns2(self):
        self.money = App.get_running_app().money
        if self.money > self.price2:
            self.guns2 += 1
            App.get_running_app().damage += 5
            App.get_running_app().return_damage = count(App.get_running_app().damage)
            self.return_guns2 = count(self.guns2)
            self.money -= self.price2
            App.get_running_app().money -= self.price2
            self.price2 *= 1.1
            self.price2 = int(self.price2)
            App.get_running_app().return_money = count(self.money)
            self.return_price2 = count(self.price2)
    def up_guns3(self):
        self.money = App.get_running_app().money
        if self.money > self.price3:
            self.guns3 += 1
            App.get_running_app().damage += 20
            App.get_running_app().return_damage = count(App.get_running_app().damage)
            self.return_guns3 = count(self.guns3)
            self.money -= self.price3
            App.get_running_app().money -= self.price3
            self.price3 *= 1
            self.price3 = int(self.price3)
            App.get_running_app().return_money = count(self.money)
            self.return_price3 = count(self.price3)
class Manager(ScreenManager):

    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)

class ScreensApp(MDApp):
    money = ObjectProperty(0)
    damage = ObjectProperty(1)
    return_damage = StringProperty('1')
    return_money = StringProperty('0')
    def build(self):
        m = Manager(transition=NoTransition())
        return m

if __name__ == "__main__":
    ScreensApp().run()


