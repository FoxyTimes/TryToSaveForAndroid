from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.clock import Clock
import sqlite3
import datetime





connect = sqlite3.connect('money.db')

cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS data(
    id INTEGER,
    sql_money INTEGER,
    sql_damage INTEGER,
    sql_plus INTEGER,
    sql_health INTEGER
    )
""")
connect.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS time(
    id INTEGER,
    last_start INTEGER
    )
""")
connect.commit()


cursor.execute("""CREATE TABLE IF NOT EXISTS data_guns(
    id INTEGER,
    sql_gun1 INTEGER,
    sql_gun2 INTEGER,
    sql_gun3 INTEGER,
    sql_gun4 INTEGER,
    sql_gun5 INTEGER,
    sql_gun6 INTEGER,
    sql_gun7 INTEGER,
    sql_gun8 INTEGER,
    sql_gun9 INTEGER,
    sql_gun10 INTEGER
    )
""")

connect.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS data_moneys(
    id INTEGER,
    sql_money1 INTEGER,
    sql_money2 INTEGER,
    sql_money3 INTEGER,
    sql_money4 INTEGER,
    sql_money5 INTEGER,
    sql_money6 INTEGER,
    sql_money7 INTEGER,
    sql_money8 INTEGER,
    sql_money9 INTEGER,
    sql_money10 INTEGER
    )
""")

connect.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS data_price_guns(
    id INTEGER,
    sql_price_gun1 INTEGER,
    sql_price_gun2 INTEGER,
    sql_price_gun3 INTEGER,
    sql_price_gun4 INTEGER,
    sql_price_gun5 INTEGER,
    sql_price_gun6 INTEGER,
    sql_price_gun7 INTEGER,
    sql_price_gun8 INTEGER,
    sql_price_gun9 INTEGER,
    sql_price_gun10 INTEGER
    )
""")

connect.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS data_price_guns(
    id INTEGER,
    sql_price_gun1 INTEGER,
    sql_price_gun2 INTEGER,
    sql_price_gun3 INTEGER,
    sql_price_gun4 INTEGER,
    sql_price_gun5 INTEGER,
    sql_price_gun6 INTEGER,
    sql_price_gun7 INTEGER,
    sql_price_gun8 INTEGER,
    sql_price_gun9 INTEGER,
    sql_price_gun10 INTEGER
    )
""")

connect.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS data_price_moneys(
    id INTEGER,
    sql_price_money1 INTEGER,
    sql_price_money2 INTEGER,
    sql_price_money3 INTEGER,
    sql_price_money4 INTEGER,
    sql_price_money5 INTEGER,
    sql_price_money6 INTEGER,
    sql_price_money7 INTEGER,
    sql_price_money8 INTEGER,
    sql_price_money9 INTEGER,
    sql_price_money10 INTEGER
    )
""")

connect.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS data_skills(
    id INTEGER,
    sql_skill1 INTEGER
    )
""")

connect.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS data_price_skills(
    id INTEGER,
    sql_price_skill1 INTEGER
    )
""")

connect.commit()

cursor.close()

def sql_search_data():
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM data")
    sql_all = cursor.fetchall()
    cursor.close()
    return sql_all
def sql_search_data_guns():
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM data_guns")
    sql_all = cursor.fetchall()
    cursor.close()
    return sql_all
def sql_search_data_moneys():
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM data_moneys")
    sql_all = cursor.fetchall()
    cursor.close()
    return sql_all
def sql_search_data_price_guns():
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM data_price_guns")
    sql_all = cursor.fetchall()
    cursor.close()
    return sql_all
def sql_search_data_price_moneys():
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM data_price_moneys")
    sql_all = cursor.fetchall()
    cursor.close()
    return sql_all
def sql_search_data_skills():
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM data_skills")
    sql_all = cursor.fetchall()
    cursor.close()
    return sql_all
def sql_search_data_price_skills():
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM data_price_skills")
    sql_all = cursor.fetchall()
    cursor.close()
    return sql_all
def sql_search_time():
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM time")
    sql_all = cursor.fetchall()
    cursor.close()
    return sql_all


if not sql_search_time():
    cursor = connect.cursor()
    sql_list = [1, datetime.datetime.today()]
    cursor.execute("INSERT INTO time VALUES(?, ?);", sql_list)
    connect.commit()
    cursor.close()

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
        return str("%.1f" % (number/1000000000000000000)) + 'Qr'
    if number / 1000000000000000 > 1.0:
        return str("%.1f" % (number/1000000000000000)) + 'T'
    if number / 1000000000000 > 1.0:
        return str("%.1f" % (number/1000000000000)) + 'Kv'
    if number / 1000000000 > 1.0:
        return str("%.1f" % (number/1000000000)) + 'B'
    if number / 1000000 > 1.0:
        return str("%.1f" % (number/1000000)) + 'M'
    if number / 1000 > 1.0:
        return str("%.1f" % (number/1000)) + 'K'
    return str(int(number))

temp = """
<ScreenOne>:
    AnchorLayout:
        spacing: 20
        canvas:
            Rectangle:
                source: 'img/darkPurple.png'
                size: self.size
                pos: self.pos
    FloatLayout:
        Button:
            size_hint: 0.7, 0.23
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            background_normal: 'img/button.png'
            background_down: 'img/button.png'
            on_press:
                root.manager.current = "screen2"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        BoxLayout:
            orientation: 'vertical'
            size_hint: .4, .4
            Label:
                color: 1, 1, 0, 1
                text: 'TryToSave'
                font_size: 70

<ScreenTwo>:
    AnchorLayout:
        canvas:
            Rectangle:
                id: rec1
                source: 'img/darkPurple.png'
                size: self.size
                pos: self.pos
    FloatLayout:
        Button:
            text: 'Меню'
            font_size: self.width/2/2/1.5
            size_hint: 0.3, 0.1
            pos_hint: {'center_x': 0.15, 'center_y': 0.88}
            background_normal: 'img/btn1.png'
            background_down: 'img/btn1_pressed.png'
            on_press:
                root.manager.current = "screen1"
    FloatLayout:
        canvas:
            Rectangle:
                source: 'img/bar_money.png'
                size: self.width/3, self.height/12
                pos: 0, self.height-self.height/2/2/2/1.5
            Rectangle:
                source: 'img/bar_damage.png'
                size: self.width/3, self.height/12
                pos: self.width/3, self.height-self.height/2/2/2/1.5
            Rectangle:
                source: 'img/bar_stamina.png'
                size: self.width/3, self.height/12
                pos: 2*(self.width/3), self.height-self.height/2/2/2/1.5
            Rectangle:
                source: 'img/money_icon.png'
                size: root.width/12, root.height/20
                pos: 5, self.height-self.height/2/2/2/2
            Rectangle:
                source: 'img/damage_icon.png'
                size: root.width/12, root.height/20
                pos: 5+root.width/3, self.height-self.height/2/2/2/2
            Rectangle:
                source: 'img/stamina_icon.png'
                size: root.width/12, root.height/20
                pos: 5+root.width/3+root.width/3, self.height-self.height/2/2/2/1.8
    FloatLayout:
        BoxLayout:
            pos: self.width/11.5, self.height/3+self.height/2/2/1.65
            size_hint: 1, 1
            MDLabel:
                color: 1, 1, 1, 1
                text: str(app.return_money)
                text_size: self.width/1.1, self.height/12
                font_size: 18
            MDLabel:
                color: 1, 1, 1, 1
                text: str(app.return_damage)
                text_size: self.width/1.1, self.height/12
                font_size: 18
            MDLabel:
                color: 1, 1, 1, 1
                text: str(root.return_mana)
                text_size: self.width/1.1, self.height/12
                font_size: 18
    FloatLayout:
        BoxLayout:
            padding: 20
            spacing: 5
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            size_hint: 0.8, 0.25
            Button:
                text: 'Улучшения'
                font_size: self.width/2/2/2/2
                background_normal: 'img/btn1.png'
                on_press: root.manager.current = "screen3"
    FloatLayout:
        id: put1h
        BoxLayout:
            id: put2h
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
                pos_hint: {'center_x': 0.5, 'center_y': 0.9}
            MDProgressBar:
                id: put3h
                max: 300
                value: 0
                pos_hint: {'center_x': 0.5, 'center_y': 0.45}
                size_hint: 0.5, 0.1
                color: 0.16, 0.13, 0.175, 1
                canvas:
                    Color:
                        rgb: 1, 1, 1, 0
                    Rectangle:
                        pos: self.x+self.width/2/2/1.5, self.center_y - self.height/2.7
                        size: self.width/1.234 * (app.health / float(self.max)) if self.max else 0, 20
                        source: 'img/bar_health2.jpg'
                    Rectangle:
                        pos: self.x, self.center_y - self.height/2
                        size: self.width, 32
                        source: 'img/bar_health1.png'
                
            Button:
                background_normal: 'img/mob1.png'
                background_down: 'img/hit_mob1.png'
                size_hint: 1, 1
                on_release: root.plus_money(), root.minus_health()
    FloatLayout:
        id: screen2fl
        canvas:
            Color:
                rgb: 1, 1, 1, 0
            Rectangle:
                pos: self.center_x/3, self.center_y/1.5
                size: self.width/1.5, self.height/2
                source:app.page_for_time_total
        MDLabel:
            halign: 'center'
            font_style: 'H6'
            text: app.text_start
            color: 1, 0, 1, 0.5
            size_hint: 1, 1
            font_size: self.width/2/2/2/2
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        Button:
            text: app.podtverdit
            background_normal: app.btn1
            background_down: app.btn1_pressed
            size_hint: 0.5, 0.2
            font_size: self.width/2/2/2
            pos_hint: {'center_x': 0.5, 'center_y': 0.46}
            on_press:
                root.clear()

<ScreenThree>:
    FloatLayout:
        canvas:
            Rectangle:
                source: 'img/darkPurple.png'
                size: self.size
                pos: self.pos
            Rectangle:
                source: 'img/bar_money.png'
                size: self.width/3, self.height/12
                pos: self.width/20, self.height-self.height/1.07
            Rectangle:
                source: 'img/bar_damage.png'
                size: self.width/3, self.height/12
                pos: self.width/2.5, self.height-self.height/1.07
            Rectangle:
                source: 'img/money_icon.png'
                size: self.width/12, self.height/20
                pos: self.width/18, self.height-self.height/1.09
            Rectangle:
                source: 'img/damage_icon.png'
                size: self.width/12, self.height/20
                pos: self.width/2.4, self.height-self.height/1.09
        MDLabel:
            halign: 'center'
            font_style: 'H6'
            text: app.return_money
            color: 1, 1, 1, 1
            size_hint: 1, 1
            font_size: 15
            pos_hint: {'center_x': 0.2, 'center_y': 0.11}
        MDLabel:
            halign: 'center'
            font_style: 'H6'
            text: app.return_damage
            color: 1, 1, 1, 1
            size_hint: 1, 1
            font_size: 15
            pos_hint: {'center_x': 0.55, 'center_y': 0.11}
        BoxLayout:
            pos_hint: {'center_x': 0.5, 'center_y': 0.85}
            size_hint: 1, .09
            Button:
                text: 'скилы'
                background_normal: 'img/btn1.png'
                background_down: 'img/btn1_pressed.png'
                size_hint: 1, 1.7
                font_size: 15
                on_press:
                    root.manager.current = "screen5"
            Button:
                text: 'Урон'
                background_normal: 'img/btn1.png'
                background_down: 'img/btn1_pressed.png'
                size_hint: 1.5, 1.7
                font_size: 15
            Button:
                text: 'деньги'
                background_normal: 'img/btn1.png'
                background_down: 'img/btn1_pressed.png'
                size_hint: 1, 1.7
                font_size: 15
                on_press:
                    root.manager.current = "screen4"
        ScrollView:
            size_hint_y: 0.6
            do_scroll_x: False
            do_scroll_y: True
            pos_hint: {'x':0.025, 'y': .2}
            GridLayout:
                size:(root.width/2+root.width/2/2+root.width/2/2/1.25, root.height+root.height)
                size_hint_x: None
                size_hint_y: None
                spacing: 30
                padding: 10
                cols: 1
                height: self.minimum_height
                canvas:
                    Rectangle:
                        source: 'img/background.jpg'
                        size: self.size
                        pos: self.pos
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade1.png'
                            size: self.size[0]/3.7, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.6, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page1.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon2.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.5
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
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
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+ 1 урон'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price1)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_guns1()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade2.png'
                            size: self.size[0]/3.7, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.6, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page1.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon2.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.5
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
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
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+ 5 урона'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price2)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_guns2()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade3.png'
                            size: self.size[0]/3.7, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.6, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page1.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon2.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.5
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
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
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+ 20 урона'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price3)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_guns3()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade4.png'
                            size: self.size[0]/3.7, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.6, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page1.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon2.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.5
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_guns4)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Ультра'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'лазер'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+ 50 урон'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price4)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_guns4()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade5.png'
                            size: self.size[0]/3.7, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.6, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page1.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon2.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.5
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_guns5)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Бластер'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+ 100 урона'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price5)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_guns5()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade6.png'
                            size: self.size[0]/3.7, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.6, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page1.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon2.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.7
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_guns6)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Ультра'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Плазмопушка'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+ 200 урон'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price6)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_guns6()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade7.png'
                            size: self.size[0]/3.7, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.6, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page1.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon2.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.5
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_guns7)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Торпеда'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+ 500 урон'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price7)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 15
                        on_press: root.up_guns7()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade8.png'
                            size: self.size[0]/3.7, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.6, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page1.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon2.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.5
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_guns8)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'ЭМИ орудие'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+ 1.0K урон'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price8)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_guns8()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade9.png'
                            size: self.size[0]/3.7, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.6, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page1.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon2.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.7
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_guns9)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'ускоритель'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'частиц'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+ 2.0K урон'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price9)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_guns9()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade10.png'
                            size: self.size[0]/3.7, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.6, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page1.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon2.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.5
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_guns10)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Гипер'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'ракета'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+ 5.0K урон'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price10)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_guns10()
        BoxLayout:
            spacing: 20
            pos_hint: {'center_x': 0.85, 'center_y': 0.1}
            spacing: 10
            size_hint: .25, .15
            Button:
                size_hint: 1.4, 1
                text: 'назад'
                background_normal: 'img/btn1.png'
                background_down: 'img/btn1_pressed.png'
                on_press:
                    root.manager.current = "screen2"


<ScreenFour>:
    FloatLayout:
        canvas:
            Rectangle:
                source: 'img/darkPurple.png'
                size: self.size
                pos: self.pos
            Rectangle:
                source: 'img/bar_money.png'
                size: self.width/3, self.height/12
                pos: self.width/20, self.height-self.height/1.07
            Rectangle:
                source: 'img/fon3.jpg'
                size: self.size[0]-self.width/1.35, self.size[1]/2/2/3
                pos: self.pos[0]+self.width/2/1.2, self.pos[1]+self.height/2/2/2/2
            Rectangle:
                source: 'img/page3.png'
                size: self.size[0]-self.width/1.35, self.size[1]/2/2/3
                pos: self.pos[0]+self.width/2/1.2, self.pos[1]+self.height/2/2/2/2
            Rectangle:
                source: 'img/money_icon.png'
                size: self.width/12, self.height/20
                pos: self.width/18, self.height-self.height/1.09
        MDLabel:
            halign: 'center'
            font_style: 'H6'
            text: app.return_money
            color: 1, 1, 1, 1
            size_hint: 1, 1
            font_size: 15
            pos_hint: {'center_x': 0.2, 'center_y': 0.11}
        MDLabel:
            halign: 'center'
            font_style: 'H6'
            text: app.return_plus + '/клик'
            color: 1, 0.5, 1, 1
            size_hint: 1, 1
            font_size: 15
            pos_hint: {'center_x': 0.55, 'center_y': 0.11}
        BoxLayout:
            pos_hint: {'center_x': 0.5, 'center_y': 0.85}
            size_hint: 1, .09
            Button:
                text: 'урон'
                background_normal: 'img/btn1.png'
                background_down: 'img/btn1_pressed.png'
                size_hint: 1, 1.7
                font_size: 15
                on_press:
                    root.manager.current = "screen3"
            Button:
                text: 'Деньги'
                background_normal: 'img/btn1.png'
                background_down: 'img/btn1_pressed.png'
                size_hint: 1.5, 1.7
                font_size: 15
            Button:
                text: 'скиллы'
                background_normal: 'img/btn1.png'
                background_down: 'img/btn1_pressed.png'
                size_hint: 1, 1.7
                font_size: 15
                on_press:
                    root.manager.current = "screen5"
        ScrollView:
            size_hint_y: 0.6
            do_scroll_x: False
            do_scroll_y: True
            pos_hint: {'x':0.025, 'y': .2}
            GridLayout:
                size:(root.width/2+root.width/2/2+root.width/2/2/1.25, root.height+root.height)
                size_hint_x: None
                size_hint_y: None
                spacing: 30
                padding: 10
                cols: 1
                height: self.minimum_height
                canvas:
                    Rectangle:
                        source: 'img/background.jpg'
                        size: self.size
                        pos: self.pos
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon5.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade_money1.png'
                            size: self.size[0]/3.7, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.6, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page5.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon4.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.5
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_money1)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Мини'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'реактор'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+1/клик'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price_money1)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_money1()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon5.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade_money2.png'
                            size: self.size[0]/3.7, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.6, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page5.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon4.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.5
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_money2)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Малый'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'реактор'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+5/клик'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price_money2)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_money2()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon5.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade_money3.png'
                            size: self.size[0]/3.7, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.6, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page5.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon4.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.5
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_money3)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Средний'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'реактор'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+20/клик'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price_money3)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_money3()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon5.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade_money4.png'
                            size: self.size[0]/3.7, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.6, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page5.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon4.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.5
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_money4)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Большой'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'реактор'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+50/клик'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price_money4)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_money4()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon5.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade_money5.png'
                            size: self.size[0]/3.7, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.6, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page5.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon4.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.5
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_money5)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Гипер'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'реактор'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+100/клик'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price_money5)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_money5()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon5.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade_money6.png'
                            size: self.size[0]/4.5, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.2, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page5.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon4.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.7
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_money6)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Энергощит'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+200/клик'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price_money6)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_money6()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon5.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade_money7.png'
                            size: self.size[0]/4.5, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.2, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page5.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon4.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.5
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_money7)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Сильный'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'энергощит'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+500/клик'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price_money7)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 15
                        on_press: root.up_money7()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon5.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade_money8.png'
                            size: self.size[0]/4.5, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.2, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page5.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon4.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.5
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_money8)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Генератор'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'сверх'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'топлива'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+1.0K/клик'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price_money8)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_money8()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon5.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade_money9.png'
                            size: self.size[0]/4.5, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.2, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page5.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon4.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.7
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_money9)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'генератор'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'гравитации'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+2.0K/клик'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price_money9)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_money9()
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon5.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade_money10.png'
                            size: self.size[0]/4.5, self.size[1]/2
                            pos: self.pos[0]+self.width/2/3/2/1.2, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page5.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon4.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.5
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_money10)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Генератор'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'материи'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+5.0K/клик'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price_money10)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_money10()
        BoxLayout:
            spacing: 20
            pos_hint: {'center_x': 0.85, 'center_y': 0.1}
            spacing: 10
            size_hint: .25, .15
            Button:
                size_hint: 1.4, 1
                text: 'назад'
                background_normal: 'img/btn1.png'
                background_down: 'img/btn1_pressed.png'
                on_press:
                    root.manager.current = "screen2"
<ScreenFive>:
    FloatLayout:
        canvas:
            Rectangle:
                source: 'img/darkPurple.png'
                size: self.size
                pos: self.pos
            Rectangle:
                source: 'img/bar_money.png'
                size: self.width/3, self.height/12
                pos: self.width/20, self.height-self.height/1.07
            Rectangle:
                source: 'img/fon3.jpg'
                size: self.size[0]-self.width/1.35, self.size[1]/2/2/3
                pos: self.pos[0]+self.width/2/1.2, self.pos[1]+self.height/2/2/2/2
            Rectangle:
                source: 'img/page3.png'
                size: self.size[0]-self.width/1.35, self.size[1]/2/2/3
                pos: self.pos[0]+self.width/2/1.2, self.pos[1]+self.height/2/2/2/2
            Rectangle:
                source: 'img/money_icon.png'
                size: self.width/12, self.height/20
                pos: self.width/18, self.height-self.height/1.09
        MDLabel:
            halign: 'center'
            font_style: 'H6'
            text: app.return_money
            color: 1, 1, 1, 1
            size_hint: 1, 1
            font_size: 15
            pos_hint: {'center_x': 0.2, 'center_y': 0.11}
        MDLabel:
            halign: 'center'
            font_style: 'H6'
            text: app.return_money_in_sec + '/сек'
            color: 1, 0.5, 1, 1
            size_hint: 1, 1
            font_size: 15
            pos_hint: {'center_x': 0.55, 'center_y': 0.11}
        BoxLayout:
            pos_hint: {'center_x': 0.5, 'center_y': 0.85}
            size_hint: 1, .09
            Button:
                text: 'деньги'
                background_normal: 'img/btn1.png'
                background_down: 'img/btn1_pressed.png'
                size_hint: 1, 1.7
                font_size: 15
                on_press:
                    root.manager.current = "screen4"
            Button:
                text: 'Скиллы'
                background_normal: 'img/btn1.png'
                background_down: 'img/btn1_pressed.png'
                size_hint: 1.5, 1.7
                font_size: 15
                on_press:
                    root.manager.current = "screen5"
            Button:
                text: 'урон'
                background_normal: 'img/btn1.png'
                background_down: 'img/btn1_pressed.png'
                size_hint: 1, 1.7
                font_size: 15
                on_press:
                    root.manager.current = "screen3"
        ScrollView:
            size_hint_y: 0.6
            do_scroll_x: False
            do_scroll_y: True
            pos_hint: {'x':0.025, 'y': .2}
            GridLayout:
                size:(root.width/2+root.width/2/2+root.width/2/2/1.25, root.height/5)
                size_hint_x: None
                size_hint_y: None
                spacing: 30
                padding: 10
                cols: 1
                height: self.minimum_height
                canvas:
                    Rectangle:
                        source: 'img/background.jpg'
                        size: self.size
                        pos: self.pos
                FloatLayout:
                    canvas:
                        Rectangle:
                            source: 'img/page.jpg'
                            size: self.size[0]-self.width/3, self.size[1]+self.height/2/2/2
                            pos: self.pos[0], self.pos[1]-5
                        Rectangle:
                            source: 'img/fon6.jpg'
                            size: self.size[0]/3.4, self.size[1]/1.4
                            pos: self.pos[0]+self.width/2/3/2/2/2, self.pos[1]+self.height/2/3
                        Rectangle:
                            source: 'img/upgrade_skill1.png'
                            size: self.size[0]/4.5, self.size[1]/1.8
                            pos: self.pos[0]+self.width/2/3/2/1.2, self.pos[1]+self.height/2/2
                        Rectangle:
                            source: 'img/page6.png'
                            size: self.size[0]/2.5, self.size[1]+self.height/2/2
                            pos: self.pos[0]-self.width/2/2/2/2/4, self.pos[1]-self.height/2/2/2
                        Rectangle:
                            source: 'img/fon7.jpg'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                        Rectangle:
                            source: 'img/page2.png'
                            size: self.size[0]-self.width/1.35, self.size[1]+self.height/2/2/8
                            pos: self.pos[0]+self.width/2/1.35, self.pos[1]
                    BoxLayout:
                        size_hint: 1, 0.5
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.65, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H4'
                            text: 'lvl ' + str(root.return_skill1)
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 15
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'Накопитель'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: 'энергии'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 10
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                        MDLabel:
                            halign: 'center'
                            font_style: 'H6'
                            text: '+1/сек'
                            color: 0.5, 1, 0.5, 1
                            size_hint: 1, 1
                            font_size: 12
                            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
                    Button:
                        size_hint: None, None
                        size: root.width/3, root.height/5
                        pos_hint: {'center_x': 0.835, 'center_y': 0.5}
                        text: str(root.return_price_skill1)
                        color: 1, 0.85, 0.1, 1
                        background_normal: 'img/btn1.png'
                        background_down: 'img/btn1_pressed.png'
                        font_size: 20
                        on_press: root.up_skill1()
        BoxLayout:
            spacing: 20
            pos_hint: {'center_x': 0.85, 'center_y': 0.1}
            spacing: 10
            size_hint: .25, .15
            Button:
                size_hint: 1.4, 1
                text: 'назад'
                background_normal: 'img/btn1.png'
                background_down: 'img/btn1_pressed.png'
                on_press:
                    root.manager.current = "screen2"

            
    
                
<Manager>:
    id: screen_manager
    screen_one: screen_one
    screen_two: screen_two
    screen_three: screen_three
    screen_four: screen_four
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
    ScreenFour:
        id: screen_four
        name: "screen4"
        manager: screen_manager
    ScreenFive:
        id: screen_five
        name: "screen5"
        manager: screen_manager
        """

Builder.load_string(temp)

class ScreenOne(Screen):
    def __init__(self, **kwargs):
        super(ScreenOne, self).__init__(**kwargs)
class ScreenTwo(Screen):
    if not sql_search_data():
        return_health = StringProperty('300')
    else:
        return_health = StringProperty(count(sql_search_data()[0][4]))
    return_mana = StringProperty('10')
    def __init__(self, **kwargs):
        super(ScreenTwo, self).__init__(**kwargs)
        self.damage = App.get_running_app().damage
        self.health = App.get_running_app().health
        self.money = App.get_running_app().money
        self.mana = 10
        self.return_mana = count(self.mana)
        if not sql_search_data():
            cursor = connect.cursor()
            sql_list = [1, self.money, self.damage, App.get_running_app().plus, self.health]
            cursor.execute("INSERT INTO data VALUES(?, ?, ?, ?, ?);", sql_list)
            connect.commit()
            cursor.close()
    def clear(self):
        self.ids.screen2fl.clear_widgets()
        self.ids.screen2fl.canvas.clear()
    def plus_money(self):
        self.check_click = 1
        if self.check_click == 1:
            self.check_click = 0
            self.money = App.get_running_app().money
            self.money += App.get_running_app().plus
            App.get_running_app().money = self.money
            App.get_running_app().return_money = count(self.money)
            self.update_sql_money()
    def minus_health(self):
        self.check_click = 1
        if self.check_click == 1:
            self.check_click = 0
            check = self.health - self.get_damage()
            if check <= 0:
                self.health = 300 + self.get_damage()
                App.get_running_app().money += 100
            self.health -= self.get_damage()
            self.return_health = count(self.health)
            App.get_running_app().return_money = count(App.get_running_app().money)
            self.update_sql_health()
            App.get_running_app().health = self.health
    def get_damage(self):
        return App.get_running_app().damage
    def update_sql_money(self):
        cursor = connect.cursor()
        sql_update_money = """Update data set sql_money = ? where id = ?"""
        data = (self.money, 1)
        cursor.execute(sql_update_money, data)
        connect.commit()
        cursor.close()
    def update_sql_health(self):
        cursor = connect.cursor()
        sql_update_health = """Update data set sql_health = ? where id = ?"""
        data = (self.health, 1)
        cursor.execute(sql_update_health, data)
        connect.commit()
        cursor.close()
class ScreenThree(Screen):
    if not sql_search_data_guns():
        return_guns1 = StringProperty('1')
        return_guns2 = StringProperty('0')
        return_guns3 = StringProperty('0')
        return_guns4 = StringProperty('0')
        return_guns5 = StringProperty('0')
        return_guns6 = StringProperty('0')
        return_guns7 = StringProperty('0')
        return_guns8 = StringProperty('0')
        return_guns9 = StringProperty('0')
        return_guns10 = StringProperty('0')
    else:
        return_guns1 = StringProperty(str(count(sql_search_data_guns()[0][1])))
        return_guns2 = StringProperty(str(count(sql_search_data_guns()[0][2])))
        return_guns3 = StringProperty(str(count(sql_search_data_guns()[0][3])))
        return_guns4 = StringProperty(str(count(sql_search_data_guns()[0][4])))
        return_guns5 = StringProperty(str(count(sql_search_data_guns()[0][5])))
        return_guns6 = StringProperty(str(count(sql_search_data_guns()[0][6])))
        return_guns7 = StringProperty(str(count(sql_search_data_guns()[0][7])))
        return_guns8 = StringProperty(str(count(sql_search_data_guns()[0][8])))
        return_guns9 = StringProperty(str(count(sql_search_data_guns()[0][9])))
        return_guns10 = StringProperty(str(count(sql_search_data_guns()[0][10])))
    if not sql_search_data_price_guns():
        return_price1 = StringProperty('100')
        return_price2 = StringProperty('1.0K')
        return_price3 = StringProperty('10.0K')
        return_price4 = StringProperty('100.0K')
        return_price5 = StringProperty('1.0M')
        return_price6 = StringProperty('10.0M')
        return_price7 = StringProperty('100.0M')
        return_price8 = StringProperty('1.0B')
        return_price9 = StringProperty('10.0B')
        return_price10 = StringProperty('100.0B')
    else:
        return_price1 = StringProperty(str(count(sql_search_data_price_guns()[0][1])))
        return_price2 = StringProperty(str(count(sql_search_data_price_guns()[0][2])))
        return_price3 = StringProperty(str(count(sql_search_data_price_guns()[0][3])))
        return_price4 = StringProperty(str(count(sql_search_data_price_guns()[0][4])))
        return_price5 = StringProperty(str(count(sql_search_data_price_guns()[0][5])))
        return_price6 = StringProperty(str(count(sql_search_data_price_guns()[0][6])))
        return_price7 = StringProperty(str(count(sql_search_data_price_guns()[0][7])))
        return_price8 = StringProperty(str(count(sql_search_data_price_guns()[0][8])))
        return_price9 = StringProperty(str(count(sql_search_data_price_guns()[0][9])))
        return_price10 = StringProperty(str(count(sql_search_data_price_guns()[0][10])))
    def __init__(self, **kwargs):
        super(ScreenThree, self).__init__(**kwargs)
        if not sql_search_data_guns():
            self.guns1 = 1
            self.guns2 = 0
            self.guns3 = 0
            self.guns4 = 0
            self.guns5 = 0
            self.guns6 = 0
            self.guns7 = 0
            self.guns8 = 0
            self.guns9 = 0
            self.guns10 = 0
        else:
            self.guns1 = ObjectProperty(sql_search_data_guns()[0][1])
            self.guns2 = ObjectProperty(sql_search_data_guns()[0][2])
            self.guns3 = ObjectProperty(sql_search_data_guns()[0][3])
            self.guns4 = ObjectProperty(sql_search_data_guns()[0][4])
            self.guns5 = ObjectProperty(sql_search_data_guns()[0][5])
            self.guns6 = ObjectProperty(sql_search_data_guns()[0][6])
            self.guns7 = ObjectProperty(sql_search_data_guns()[0][7])
            self.guns8 = ObjectProperty(sql_search_data_guns()[0][8])
            self.guns9 = ObjectProperty(sql_search_data_guns()[0][9])
            self.guns10 = ObjectProperty(sql_search_data_guns()[0][10])
            self.guns1 = sql_search_data_guns()[0][1]
            self.guns2 = sql_search_data_guns()[0][2]
            self.guns3 = sql_search_data_guns()[0][3]
            self.guns4 = sql_search_data_guns()[0][4]
            self.guns5 = sql_search_data_guns()[0][5]
            self.guns6 = sql_search_data_guns()[0][6]
            self.guns7 = sql_search_data_guns()[0][7]
            self.guns8 = sql_search_data_guns()[0][8]
            self.guns9 = sql_search_data_guns()[0][9]
            self.guns10 = sql_search_data_guns()[0][10]
        if not sql_search_data_guns():
            self.price1 = 100
            self.price2 = 1000
            self.price3 = 10000
            self.price4 = 100000
            self.price5 = 1000000
            self.price6 = 10000000
            self.price7 = 100000000
            self.price8 = 1000000000
            self.price9 = 10000000000
            self.price10 = 100000000000
        else:
            self.price1 = ObjectProperty(sql_search_data_guns()[0][1])
            self.price2 = ObjectProperty(sql_search_data_guns()[0][2])
            self.price3 = ObjectProperty(sql_search_data_guns()[0][3])
            self.price4 = ObjectProperty(sql_search_data_guns()[0][4])
            self.price5 = ObjectProperty(sql_search_data_guns()[0][5])
            self.price6 = ObjectProperty(sql_search_data_guns()[0][6])
            self.price7 = ObjectProperty(sql_search_data_guns()[0][7])
            self.price8 = ObjectProperty(sql_search_data_guns()[0][8])
            self.price9 = ObjectProperty(sql_search_data_guns()[0][9])
            self.price10 = ObjectProperty(sql_search_data_guns()[0][10])
            self.price1 = sql_search_data_price_guns()[0][1]
            self.price2 = sql_search_data_price_guns()[0][2]
            self.price3 = sql_search_data_price_guns()[0][3]
            self.price4 = sql_search_data_price_guns()[0][4]
            self.price5 = sql_search_data_price_guns()[0][5]
            self.price6 = sql_search_data_price_guns()[0][6]
            self.price7 = sql_search_data_price_guns()[0][7]
            self.price8 = sql_search_data_price_guns()[0][8]
            self.price9 = sql_search_data_price_guns()[0][9]
            self.price10 = sql_search_data_price_guns()[0][10]
        self.money = App.get_running_app().money
        if not sql_search_data_guns():
            cursor = connect.cursor()
            sql_list = [1, self.guns1, self.guns2, self.guns3, self.guns4, self.guns5, self.guns6, self.guns7, self.guns8, self.guns9, self.guns10]
            cursor.execute("INSERT INTO data_guns VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", sql_list)
            connect.commit()
            cursor.close()
        if not sql_search_data_price_guns():
            cursor = connect.cursor()
            sql_list = [1, self.price1, self.price2, self.price3, self.price4, self.price5, self.price6, self.price7, self.price8, self.price9, self.price10]
            cursor.execute("INSERT INTO data_price_guns VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", sql_list)
            connect.commit()
            cursor.close()
    def up_guns1(self):
        self.money = App.get_running_app().money
        if self.money >= self.price1:
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
            self.update_sql_damage()
            self.update_guns()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_guns2(self):
        self.money = App.get_running_app().money
        if self.money >= self.price2:
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
            self.update_sql_damage()
            self.update_guns()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_guns3(self):
        self.money = App.get_running_app().money
        if self.money >= self.price3:
            self.guns3 += 1
            App.get_running_app().damage += 20
            App.get_running_app().return_damage = count(App.get_running_app().damage)
            self.return_guns3 = count(self.guns3)
            self.money -= self.price3
            App.get_running_app().money -= self.price3
            self.price3 *= 1.1
            self.price3 = int(self.price3)
            App.get_running_app().return_money = count(self.money)
            self.return_price3 = count(self.price3)
            self.update_sql_damage()
            self.update_guns()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_guns4(self):
        self.money = App.get_running_app().money
        if self.money >= self.price4:
            self.guns4 += 1
            App.get_running_app().damage += 50
            App.get_running_app().return_damage = count(App.get_running_app().damage)
            self.return_guns4 = count(self.guns4)
            self.money -= self.price4
            App.get_running_app().money -= self.price4
            self.price4 *= 1.1
            self.price4 = int(self.price4)
            App.get_running_app().return_money = count(self.money)
            self.return_price4 = count(self.price4)
            self.update_sql_damage()
            self.update_guns()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_guns5(self):
        self.money = App.get_running_app().money
        if self.money >= self.price5:
            self.guns5 += 1
            App.get_running_app().damage += 100
            App.get_running_app().return_damage = count(App.get_running_app().damage)
            self.return_guns5 = count(self.guns5)
            self.money -= self.price5
            App.get_running_app().money -= self.price5
            self.price5*= 1.1
            self.price5 = int(self.price5)
            App.get_running_app().return_money = count(self.money)
            self.return_price5 = count(self.price5)
            self.update_sql_damage()
            self.update_guns()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_guns6(self):
        self.money = App.get_running_app().money
        if self.money >= self.price6:
            self.guns6 += 1
            App.get_running_app().damage += 200
            App.get_running_app().return_damage = count(App.get_running_app().damage)
            self.return_guns6 = count(self.guns6)
            self.money -= self.price6
            App.get_running_app().money -= self.price6
            self.price6*= 1.1
            self.price6 = int(self.price6)
            App.get_running_app().return_money = count(self.money)
            self.return_price6 = count(self.price6)
            self.update_sql_damage()
            self.update_guns()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_guns7(self):
        self.money = App.get_running_app().money
        if self.money >= self.price7:
            self.guns7 += 1
            App.get_running_app().damage += 500
            App.get_running_app().return_damage = count(App.get_running_app().damage)
            self.return_guns7 = count(self.guns7)
            self.money -= self.price7
            App.get_running_app().money -= self.price7
            self.price7*= 1.1
            self.price7 = int(self.price7)
            App.get_running_app().return_money = count(self.money)
            self.return_price7 = count(self.price7)
            self.update_sql_damage()
            self.update_guns()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_guns8(self):
        self.money = App.get_running_app().money
        if self.money >= self.price8:
            self.guns8 += 1
            App.get_running_app().damage += 1000
            App.get_running_app().return_damage = count(App.get_running_app().damage)
            self.return_guns8 = count(self.guns8)
            self.money -= self.price8
            App.get_running_app().money -= self.price8
            self.price8 *= 1.1
            self.price8 = int(self.price8)
            App.get_running_app().return_money = count(self.money)
            self.return_price8 = count(self.price8)
            self.update_sql_damage()
            self.update_guns()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_guns9(self):
        self.money = App.get_running_app().money
        if self.money >= self.price9:
            self.guns9 += 1
            App.get_running_app().damage += 2000
            App.get_running_app().return_damage = count(App.get_running_app().damage)
            self.return_guns9 = count(self.guns9)
            self.money -= self.price9
            App.get_running_app().money -= self.price9
            self.price9 *= 1.1
            self.price9 = int(self.price9)
            App.get_running_app().return_money = count(self.money)
            self.return_price9 = count(self.price9)
            self.update_sql_damage()
            self.update_guns()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_guns10(self):
        self.money = App.get_running_app().money
        if self.money >= self.price10:
            self.guns10 += 1
            App.get_running_app().damage += 5000
            App.get_running_app().return_damage = count(App.get_running_app().damage)
            self.return_guns10 = count(self.guns10)
            self.money -= self.price10
            App.get_running_app().money -= self.price10
            self.price10 *= 1.1
            self.price10 = int(self.price10)
            App.get_running_app().return_money = count(self.money)
            self.return_price10 = count(self.price10)
            self.update_sql_damage()
            self.update_guns()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def update_sql_money(self):
        cursor = connect.cursor()
        sql_update_money = """Update data set sql_money = ? where id = ?"""
        data = (self.money, 1)
        cursor.execute(sql_update_money, data)
        connect.commit()
        cursor.close()
    def update_sql_damage(self):
        cursor = connect.cursor()
        sql_update_damage = """Update data set sql_damage = ? where id = ?"""
        data = (App.get_running_app().damage, 1)
        cursor.execute(sql_update_damage, data)
        connect.commit()
        cursor.close()
    def update_guns(self):
        cursor = connect.cursor()
        sql_update_gun = """Update data_guns set sql_gun1 = ? where id = ?"""
        data = (self.guns1, 1)
        cursor.execute(sql_update_gun, data)
        sql_update_gun = """Update data_guns set sql_gun2 = ? where id = ?"""
        data = (self.guns2, 1)
        cursor.execute(sql_update_gun, data)
        sql_update_gun = """Update data_guns set sql_gun3 = ? where id = ?"""
        data = (self.guns3, 1)
        cursor.execute(sql_update_gun, data)
        sql_update_gun = """Update data_guns set sql_gun4 = ? where id = ?"""
        data = (self.guns4, 1)
        cursor.execute(sql_update_gun, data)
        sql_update_gun = """Update data_guns set sql_gun5 = ? where id = ?"""
        data = (self.guns5, 1)
        cursor.execute(sql_update_gun, data)
        sql_update_gun = """Update data_guns set sql_gun6 = ? where id = ?"""
        data = (self.guns6, 1)
        cursor.execute(sql_update_gun, data)
        sql_update_gun = """Update data_guns set sql_gun7 = ? where id = ?"""
        data = (self.guns7, 1)
        cursor.execute(sql_update_gun, data)
        sql_update_gun = """Update data_guns set sql_gun8 = ? where id = ?"""
        data = (self.guns8, 1)
        cursor.execute(sql_update_gun, data)
        sql_update_gun = """Update data_guns set sql_gun9 = ? where id = ?"""
        data = (self.guns9, 1)
        cursor.execute(sql_update_gun, data)
        sql_update_gun = """Update data_guns set sql_gun10 = ? where id = ?"""
        data = (self.guns10, 1)
        cursor.execute(sql_update_gun, data)
        connect.commit()
        cursor.close()
    def update_prices(self):
        cursor = connect.cursor()
        sql_update_price = """Update data_price_guns set sql_price_gun1 = ? where id = ?"""
        data = (self.price1, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_guns set sql_price_gun2 = ? where id = ?"""
        data = (self.price2, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_guns set sql_price_gun3 = ? where id = ?"""
        data = (self.price3, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_guns set sql_price_gun4 = ? where id = ?"""
        data = (self.price4, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_guns set sql_price_gun5 = ? where id = ?"""
        data = (self.price5, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_guns set sql_price_gun6 = ? where id = ?"""
        data = (self.price6, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_guns set sql_price_gun7 = ? where id = ?"""
        data = (self.price7, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_guns set sql_price_gun8 = ? where id = ?"""
        data = (self.price8, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_guns set sql_price_gun9 = ? where id = ?"""
        data = (self.price9, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_guns set sql_price_gun10 = ? where id = ?"""
        data = (self.price10, 1)
        cursor.execute(sql_update_price, data)
        connect.commit()
        cursor.close()

class ScreenFour(Screen):
    if not sql_search_data_moneys():
        return_money1 = StringProperty('1')
        return_money2 = StringProperty('0')
        return_money3 = StringProperty('0')
        return_money4 = StringProperty('0')
        return_money5 = StringProperty('0')
        return_money6 = StringProperty('0')
        return_money7 = StringProperty('0')
        return_money8 = StringProperty('0')
        return_money9 = StringProperty('0')
        return_money10 = StringProperty('0')
    else:
        return_money1 = StringProperty(str(count(sql_search_data_moneys()[0][1])))
        return_money2 = StringProperty(str(count(sql_search_data_moneys()[0][2])))
        return_money3 = StringProperty(str(count(sql_search_data_moneys()[0][3])))
        return_money4 = StringProperty(str(count(sql_search_data_moneys()[0][4])))
        return_money5 = StringProperty(str(count(sql_search_data_moneys()[0][5])))
        return_money6 = StringProperty(str(count(sql_search_data_moneys()[0][6])))
        return_money7 = StringProperty(str(count(sql_search_data_moneys()[0][7])))
        return_money8 = StringProperty(str(count(sql_search_data_moneys()[0][8])))
        return_money9 = StringProperty(str(count(sql_search_data_moneys()[0][9])))
        return_money10 = StringProperty(str(count(sql_search_data_moneys()[0][10])))
    if not sql_search_data_guns():
        return_price_money1 = StringProperty('100')
        return_price_money2 = StringProperty('1.0K')
        return_price_money3 = StringProperty('10.0K')
        return_price_money4 = StringProperty('100.0K')
        return_price_money5 = StringProperty('1.0M')
        return_price_money6 = StringProperty('10.0M')
        return_price_money7 = StringProperty('100.0M')
        return_price_money8 = StringProperty('1.0B')
        return_price_money9 = StringProperty('10.0B')
        return_price_money10 = StringProperty('100.0B')
    else:
        return_price_money1 = StringProperty(str(count(sql_search_data_price_moneys()[0][1])))
        return_price_money2 = StringProperty(str(count(sql_search_data_price_moneys()[0][2])))
        return_price_money3 = StringProperty(str(count(sql_search_data_price_moneys()[0][3])))
        return_price_money4 = StringProperty(str(count(sql_search_data_price_moneys()[0][4])))
        return_price_money5 = StringProperty(str(count(sql_search_data_price_moneys()[0][5])))
        return_price_money6 = StringProperty(str(count(sql_search_data_price_moneys()[0][6])))
        return_price_money7 = StringProperty(str(count(sql_search_data_price_moneys()[0][7])))
        return_price_money8 = StringProperty(str(count(sql_search_data_price_moneys()[0][8])))
        return_price_money9 = StringProperty(str(count(sql_search_data_price_moneys()[0][9])))
        return_price_money10 = StringProperty(str(count(sql_search_data_price_moneys()[0][10])))
    def __init__(self, **kwargs):
        super(ScreenFour, self).__init__(**kwargs)
        if not sql_search_data_moneys():
            self.money1 = ObjectProperty(1)
            self.money2 = ObjectProperty(0)
            self.money3 = ObjectProperty(0)
            self.money4 = ObjectProperty(0)
            self.money5 = ObjectProperty(0)
            self.money6 = ObjectProperty(0)
            self.money7 = ObjectProperty(0)
            self.money8 = ObjectProperty(0)
            self.money9 = ObjectProperty(0)
            self.money10 = ObjectProperty(0)
        else:
            self.money1 = ObjectProperty(sql_search_data_moneys()[0][1])
            self.money2 = ObjectProperty(sql_search_data_moneys()[0][2])
            self.money3 = ObjectProperty(sql_search_data_moneys()[0][3])
            self.money4 = ObjectProperty(sql_search_data_moneys()[0][4])
            self.money5 = ObjectProperty(sql_search_data_moneys()[0][5])
            self.money6 = ObjectProperty(sql_search_data_moneys()[0][6])
            self.money7 = ObjectProperty(sql_search_data_moneys()[0][7])
            self.money8 = ObjectProperty(sql_search_data_moneys()[0][8])
            self.money9 = ObjectProperty(sql_search_data_moneys()[0][9])
            self.money10 = ObjectProperty(sql_search_data_moneys()[0][10])
            self.money1 = sql_search_data_moneys()[0][1]
            self.money2 = sql_search_data_moneys()[0][2]
            self.money3 = sql_search_data_moneys()[0][3]
            self.money4 = sql_search_data_moneys()[0][4]
            self.money5 = sql_search_data_moneys()[0][5]
            self.money6 = sql_search_data_moneys()[0][6]
            self.money7 = sql_search_data_moneys()[0][7]
            self.money8 = sql_search_data_moneys()[0][8]
            self.money9 = sql_search_data_moneys()[0][9]
            self.money10 = sql_search_data_moneys()[0][10]
        if not sql_search_data_price_moneys():
            self.price_money1 = 100
            self.price_money2 = 1000
            self.price_money3 = 10000
            self.price_money4 = 100000
            self.price_money5 = 1000000
            self.price_money6 = 10000000
            self.price_money7 = 100000000
            self.price_money8 = 1000000000
            self.price_money9 = 10000000000
            self.price_money10 = 100000000000
        else:
            self.price_money1 = ObjectProperty(sql_search_data_price_moneys()[0][1])
            self.price_money2 = ObjectProperty(sql_search_data_price_moneys()[0][2])
            self.price_money3 = ObjectProperty(sql_search_data_price_moneys()[0][3])
            self.price_money4 = ObjectProperty(sql_search_data_price_moneys()[0][4])
            self.price_money5 = ObjectProperty(sql_search_data_price_moneys()[0][5])
            self.price_money6 = ObjectProperty(sql_search_data_price_moneys()[0][6])
            self.price_money7 = ObjectProperty(sql_search_data_price_moneys()[0][7])
            self.price_money8 = ObjectProperty(sql_search_data_price_moneys()[0][8])
            self.price_money9 = ObjectProperty(sql_search_data_price_moneys()[0][9])
            self.price_money10 = ObjectProperty(sql_search_data_price_moneys()[0][10])
            self.price_money1 = sql_search_data_price_moneys()[0][1]
            self.price_money2 = sql_search_data_price_moneys()[0][2]
            self.price_money3 = sql_search_data_price_moneys()[0][3]
            self.price_money4 = sql_search_data_price_moneys()[0][4]
            self.price_money5 = sql_search_data_price_moneys()[0][5]
            self.price_money6 = sql_search_data_price_moneys()[0][6]
            self.price_money7 = sql_search_data_price_moneys()[0][7]
            self.price_money8 = sql_search_data_price_moneys()[0][8]
            self.price_money9 = sql_search_data_price_moneys()[0][9]
            self.price_money10 = sql_search_data_price_moneys()[0][10]
        self.money = App.get_running_app().money
        if not sql_search_data_moneys():
            self.money1 = 1
            self.money2 = 0
            self.money3 = 0
            self.money4 = 0
            self.money5 = 0
            self.money6 = 0
            self.money7 = 0
            self.money8 = 0
            self.money9 = 0
            self.money10 = 0
            cursor = connect.cursor()
            sql_list = [1, self.money1, self.money2, self.money3, self.money4, self.money5, self.money6, self.money7, self.money8, self.money9, self.money10]
            cursor.execute("INSERT INTO data_moneys VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", sql_list)
            connect.commit()
            cursor.close()
        if not sql_search_data_price_moneys():
            cursor = connect.cursor()
            sql_list = [1, self.price_money1, self.price_money2, self.price_money3, self.price_money4, self.price_money5, self.price_money6, self.price_money7, self.price_money8, self.price_money9, self.price_money10]
            cursor.execute("INSERT INTO data_price_moneys VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", sql_list)
            connect.commit()
            cursor.close()
    def up_money1(self):
        self.money = App.get_running_app().money
        if self.money >= self.price_money1:
            self.money1 += 1
            App.get_running_app().plus += 1
            App.get_running_app().return_plus = count(App.get_running_app().plus)
            self.return_money1 = count(self.money1)
            self.money -= self.price_money1
            App.get_running_app().money -= self.price_money1
            self.price_money1 *= 1.1
            self.price_money1 = int(self.price_money1)
            App.get_running_app().return_money = count(self.money)
            self.return_price_money1 = count(self.price_money1)
            self.sql_damage_update()
            self.update_moneys()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_money2(self):
        self.money = App.get_running_app().money
        if self.money >= self.price_money2:
            self.money2 += 1
            App.get_running_app().plus += 5
            App.get_running_app().return_plus = count(App.get_running_app().plus)
            self.return_money2 = count(self.money2)
            self.money -= self.price_money2
            App.get_running_app().money -= self.price_money2
            self.price_money2 *= 1.1
            self.price_money2 = int(self.price_money2)
            App.get_running_app().return_money = count(self.money)
            self.return_price_money2 = count(self.price_money2)
            self.sql_damage_update()
            self.update_moneys()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_money3(self):
        self.money = App.get_running_app().money
        if self.money >= self.price_money3:
            self.money3 += 1
            App.get_running_app().plus += 20
            App.get_running_app().return_plus = count(App.get_running_app().plus)
            self.return_money3 = count(self.money3)
            self.money -= self.price_money3
            App.get_running_app().money -= self.price_money3
            self.price_money3 *= 1.1
            self.price_money3 = int(self.price_money3)
            App.get_running_app().return_money = count(self.money)
            self.return_price_money3 = count(self.price_money3)
            self.sql_damage_update()
            self.update_moneys()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_money4(self):
        self.money = App.get_running_app().money
        if self.money >= self.price_money4:
            self.money4 += 1
            App.get_running_app().plus += 50
            App.get_running_app().return_plus = count(App.get_running_app().plus)
            self.return_money4 = count(self.money4)
            self.money -= self.price_money4
            App.get_running_app().money -= self.price_money4
            self.price_money4 *= 1.1
            self.price_money4 = int(self.price_money4)
            App.get_running_app().return_money = count(self.money)
            self.return_price_money4 = count(self.price_money4)
            self.sql_damage_update()
            self.update_moneys()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_money5(self):
        self.money = App.get_running_app().money
        if self.money >= self.price_money5:
            self.money5 += 1
            App.get_running_app().plus += 100
            App.get_running_app().return_plus = count(App.get_running_app().plus)
            self.return_money5 = count(self.money5)
            self.money -= self.price_money5
            App.get_running_app().money -= self.price_money5
            self.price_money5 *= 1.1
            self.price_money5 = int(self.price_money5)
            App.get_running_app().return_money = count(self.money)
            self.return_price_money5 = count(self.price_money5)
            self.sql_damage_update()
            self.update_moneys()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_money6(self):
        self.money = App.get_running_app().money
        if self.money >= self.price_money6:
            self.money6 += 1
            App.get_running_app().plus += 200
            App.get_running_app().return_plus = count(App.get_running_app().plus)
            self.return_money6 = count(self.money6)
            self.money -= self.price_money6
            App.get_running_app().money -= self.price_money6
            self.price_money6 *= 1.1
            self.price_money6 = int(self.price_money6)
            App.get_running_app().return_money = count(self.money)
            self.return_price_money6 = count(self.price_money6)
            self.sql_damage_update()
            self.update_moneys()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_money7(self):
        self.money = App.get_running_app().money
        if self.money >= self.price_money7:
            self.money7 += 1
            App.get_running_app().plus += 500
            App.get_running_app().return_plus = count(App.get_running_app().plus)
            self.return_money7 = count(self.money7)
            self.money -= self.price_money7
            App.get_running_app().money -= self.price_money7
            self.price_money7 *= 1.1
            self.price_money7 = int(self.price_money7)
            App.get_running_app().return_money = count(self.money)
            self.return_price_money7 = count(self.price_money7)
            self.sql_damage_update()
            self.update_moneys()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_money8(self):
        self.money = App.get_running_app().money
        if self.money >= self.price_money8:
            self.money8 += 1
            App.get_running_app().plus += 1000
            App.get_running_app().return_plus = count(App.get_running_app().plus)
            self.return_money8 = count(self.money8)
            self.money -= self.price_money8
            App.get_running_app().money -= self.price_money8
            self.price_money8 *= 1.1
            self.price_money8 = int(self.price_money8)
            App.get_running_app().return_money = count(self.money)
            self.return_price_money8 = count(self.price_money8)
            self.sql_damage_update()
            self.update_moneys()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_money9(self):
        self.money = App.get_running_app().money
        if self.money >= self.price_money9:
            self.money9 += 1
            App.get_running_app().plus += 2000
            App.get_running_app().return_plus = count(App.get_running_app().plus)
            self.return_money9 = count(self.money9)
            self.money -= self.price_money9
            App.get_running_app().money -= self.price_money9
            self.price_money9 *= 1.1
            self.price_money9 = int(self.price_money9)
            App.get_running_app().return_money = count(self.money)
            self.return_price_money9 = count(self.price_money9)
            self.sql_damage_update()
            self.update_moneys()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def up_money10(self):
        self.money = App.get_running_app().money
        if self.money >= self.price_money10:
            self.money10 += 1
            App.get_running_app().plus += 5000
            App.get_running_app().return_plus = count(App.get_running_app().plus)
            self.return_money10 = count(self.money10)
            self.money -= self.price_money10
            App.get_running_app().money -= self.price_money10
            self.price_money10 *= 1.1
            self.price_money10 = int(self.price_money10)
            App.get_running_app().return_money = count(self.money)
            self.return_price_money10 = count(self.price_money10)
            self.sql_damage_update()
            self.update_moneys()
            self.update_prices()
            App.get_running_app().money = self.money
            self.update_sql_money()
    def sql_damage_update(self):
        cursor = connect.cursor()
        sql_update_plus = """Update data set sql_plus = ? where id = ?"""
        data = (App.get_running_app().plus, 1)
        cursor.execute(sql_update_plus, data)
        connect.commit()
        cursor.close()
    def update_sql_money(self):
        cursor = connect.cursor()
        sql_update_money = """Update data set sql_money = ? where id = ?"""
        data = (self.money, 1)
        cursor.execute(sql_update_money, data)
        connect.commit()
        cursor.close()
    def update_moneys(self):
        cursor = connect.cursor()
        sql_update_money = """Update data_moneys set sql_money1 = ? where id = ?"""
        data = (self.money1, 1)
        cursor.execute(sql_update_money, data)
        sql_update_money = """Update data_moneys set sql_money2 = ? where id = ?"""
        data = (self.money2, 1)
        cursor.execute(sql_update_money, data)
        sql_update_money = """Update data_moneys set sql_money3 = ? where id = ?"""
        data = (self.money3, 1)
        cursor.execute(sql_update_money, data)
        sql_update_money = """Update data_moneys set sql_money4 = ? where id = ?"""
        data = (self.money4, 1)
        cursor.execute(sql_update_money, data)
        sql_update_money = """Update data_moneys set sql_money5 = ? where id = ?"""
        data = (self.money5, 1)
        cursor.execute(sql_update_money, data)
        sql_update_money = """Update data_moneys set sql_money6 = ? where id = ?"""
        data = (self.money6, 1)
        cursor.execute(sql_update_money, data)
        sql_update_money = """Update data_moneys set sql_money7 = ? where id = ?"""
        data = (self.money7, 1)
        cursor.execute(sql_update_money, data)
        sql_update_money = """Update data_moneys set sql_money8 = ? where id = ?"""
        data = (self.money8, 1)
        cursor.execute(sql_update_money, data)
        sql_update_money = """Update data_moneys set sql_money9 = ? where id = ?"""
        data = (self.money9, 1)
        cursor.execute(sql_update_money, data)
        sql_update_money = """Update data_moneys set sql_money10 = ? where id = ?"""
        data = (self.money10, 1)
        cursor.execute(sql_update_money, data)
        connect.commit()
        cursor.close()
    def update_prices(self):
        cursor = connect.cursor()
        sql_update_price = """Update data_price_moneys set sql_price_money1 = ? where id = ?"""
        data = (self.price_money1, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_moneys set sql_price_money2 = ? where id = ?"""
        data = (self.price_money2, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_moneys set sql_price_money3 = ? where id = ?"""
        data = (self.price_money3, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_moneys set sql_price_money4 = ? where id = ?"""
        data = (self.price_money4, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_moneys set sql_price_money5 = ? where id = ?"""
        data = (self.price_money5, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_moneys set sql_price_money6 = ? where id = ?"""
        data = (self.price_money6, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_moneys set sql_price_money7 = ? where id = ?"""
        data = (self.price_money7, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_moneys set sql_price_money8 = ? where id = ?"""
        data = (self.price_money8, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_moneys set sql_price_money9 = ? where id = ?"""
        data = (self.price_money9, 1)
        cursor.execute(sql_update_price, data)
        sql_update_price = """Update data_price_moneys set sql_price_money10 = ? where id = ?"""
        data = (self.price_money10, 1)
        cursor.execute(sql_update_price, data)
        connect.commit()
        cursor.close()

class ScreenFive(Screen):
    if not sql_search_data_moneys():
        return_skill1 = StringProperty('0')
    else:
        return_skill1 = StringProperty(str(count(sql_search_data_skills()[0][1])))

    if not sql_search_data_guns():
        return_price_skill1 = StringProperty('100')
    else:
        return_price_skill1 = StringProperty(str(count(sql_search_data_price_skills()[0][1])))


    def __init__(self, **kwargs):
        super(ScreenFive, self).__init__(**kwargs)
        if not sql_search_data_skills():
            self.skill1 = ObjectProperty(0)
        else:
            self.skill1 = ObjectProperty(sql_search_data_skills()[0][1])
            self.skill1 = sql_search_data_skills()[0][1]
        if not sql_search_data_price_skills():
            self.price_skill1 = 100
        else:
            self.price_skill1 = ObjectProperty(sql_search_data_price_skills()[0][1])
            self.price_skill1 = sql_search_data_price_skills()[0][1]
        self.money = App.get_running_app().money
        if not sql_search_data_skills():
            self.skill1 = 0
            cursor = connect.cursor()
            sql_list = [1, self.skill1]
            cursor.execute("INSERT INTO data_skills VALUES(?, ?);", sql_list)
            connect.commit()
            cursor.close()
        if not sql_search_data_price_skills():
            cursor = connect.cursor()
            sql_list = [1, self.price_skill1]
            cursor.execute("INSERT INTO data_price_skills VALUES(?, ?);", sql_list)
            connect.commit()
            cursor.close()

    def up_skill1(self):
        self.money = App.get_running_app().money
        if self.money >= self.price_skill1:
            self.skill1 += 1
            App.get_running_app().money_in_sec += 1
            App.get_running_app().return_money_in_sec = count(App.get_running_app().money_in_sec)
            self.return_skill1 = count(self.skill1)
            self.money -= self.price_skill1
            App.get_running_app().money -= self.price_skill1
            self.price_skill1 *= 1.1
            self.price_skill1 = int(self.price_skill1)
            App.get_running_app().return_money = count(self.money)
            self.return_price_skill1 = count(self.price_skill1)
            self.update_skills()
            self.update_prices()
            self.update_sql_money()

    def update_skills(self):
        cursor = connect.cursor()
        sql_update_skill = """Update data_skills set sql_skill1 = ? where id = ?"""
        data = (self.skill1, 1)
        cursor.execute(sql_update_skill, data)
        connect.commit()
        cursor.close()

    def update_prices(self):
        cursor = connect.cursor()
        sql_update_price = """Update data_price_skills set sql_price_skill1 = ? where id = ?"""
        data = (self.price_skill1, 1)
        cursor.execute(sql_update_price, data)
        connect.commit()
        cursor.close()

    def update_sql_money(self):
        cursor = connect.cursor()
        sql_update_money = """Update data set sql_money = ? where id = ?"""
        data = (self.money, 1)
        cursor.execute(sql_update_money, data)
        connect.commit()
        cursor.close()


class Manager(ScreenManager):

    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)
    screen_four = ObjectProperty(None)
    screen_five = ObjectProperty(None)
class ScreensApp(MDApp):
    max = ObjectProperty(300)
    max = 300
    time = datetime.datetime.today() - datetime.datetime.strptime(sql_search_time()[0][1], '%Y-%m-%d %H:%M:%S.%f')
    time = int(time.total_seconds())
    if not sql_search_data():
        money = ObjectProperty(0)
    else:
        money = ObjectProperty(sql_search_data()[0][1])
    if not sql_search_data_skills():
        money_in_sec = ObjectProperty(0)
        money_in_sec = 0
    else:
        money_in_sec = ObjectProperty(sql_search_data_skills()[0][1])
        money_in_sec = sql_search_data_skills()[0][1]
    if not sql_search_data_skills():
        return_money_in_sec = StringProperty('1')
    else:
        return_money_in_sec = StringProperty(str(count(sql_search_data_skills()[0][1])))
    if not sql_search_data():
        damage = ObjectProperty(1)
    else:
        damage = ObjectProperty(sql_search_data()[0][2])
    if not sql_search_data():
        return_damage = StringProperty('1')
    else:
        return_damage = StringProperty(str(count(sql_search_data()[0][2])))
    if not sql_search_data():
        return_money = StringProperty('0')
    else:
        return_money = StringProperty(str(count(sql_search_data()[0][1])))
    if not sql_search_data():
        plus = ObjectProperty(1)
    else:
        plus = ObjectProperty(sql_search_data()[0][3])
    if not sql_search_data():
        return_plus = StringProperty('1')
    else:
        return_plus = StringProperty(str(count(sql_search_data()[0][3])))
    if not sql_search_data():
        health = ObjectProperty(300)
    else:
        health = ObjectProperty(sql_search_data()[0][4])
    if not sql_search_data():
        health = ObjectProperty(300)
    else:
        health = ObjectProperty(sql_search_data()[0][4])
    if not sql_search_data_skills():
        return_total_money_in_time = ObjectProperty(0)
        return_total_money_in_time = 0
        return_return_total_money_in_time = StringProperty('0')
    else:
        return_total_money_in_time = ObjectProperty(money_in_sec * time)
        return_total_money_in_time = money_in_sec * time
        return_return_total_money_in_time = StringProperty(str(count(return_total_money_in_time)))
        return_return_total_money_in_time = str(count(return_total_money_in_time))
    if return_total_money_in_time != 0:
        podtverdit = 'Подтвердить'
        btn1 = 'img/btn1.png'
        btn1_pressed = 'img/btn1_pressed.png'
        text_start = 'Вы получили ' + str(return_return_total_money_in_time)
        page_for_time_total = 'img/page_for_time_total.png'
    else:
        podtverdit = ''
        btn1 = 'img/clear.png'
        btn1_pressed = 'img/clear.png'
        text_start = ''
        page_for_time_total = 'img/clear.png'
    def on_start(self):
        Clock.schedule_interval(self.get_time, 1)
        time = datetime.datetime.today() - datetime.datetime.strptime(sql_search_time()[0][1], '%Y-%m-%d %H:%M:%S.%f')
        time = int(time.total_seconds())
        App.get_running_app().money += App.get_running_app().money_in_sec * time
        self.update_sql_money()
        if not sql_search_data():
            pass
        else:
            App.get_running_app().return_money = str(count(sql_search_data()[0][1]))
        print(App.get_running_app().return_total_money_in_time)
        cursor = connect.cursor()
        sql_update_money = """Update time set last_start = ? where id = ?"""
        data = (datetime.datetime.today(), 1)
        cursor.execute(sql_update_money, data)
        connect.commit()
        cursor.close()
    def get_time(self, instance):
        App.get_running_app().money += App.get_running_app().money_in_sec
        self.update_sql_money()
        if not sql_search_data():
            pass
        else:
            App.get_running_app().return_money = str(count(sql_search_data()[0][1]))
    def build(self):
        m = Manager(transition=NoTransition())
        return m
    def update_sql_money(self):
        cursor = connect.cursor()
        sql_update_money = """Update data set sql_money = ? where id = ?"""
        data = (App.get_running_app().money, 1)
        cursor.execute(sql_update_money, data)
        connect.commit()
        cursor.close()

if __name__ == "__main__":
    ScreensApp().run()

