from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.utils import platform
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.uix.scrollview import MDScrollView
from kivy.clock import Clock
import json  # importamos la libreria de python que nos permite trabajar con json
from pathlib import Path  # cargar ruta del script
from updates import Update
from db import CreateDB
import requests
import sqlite3
import db
import kivy


class SplashScreen(MDScreen):
    def on_enter(self, *args):
        print('[*ALEIX*]: Entering')
        Clock.schedule_once(self.switch_to_home, 1)

    def switch_to_home(self, dt):
        print('[*ALEIX*]: I\'m in switch_to_home')
        app = MDApp.get_running_app()
        print('[*ALEIX*]: App saved')
        app.switch_screen('login')

class ContentNavigationDrawer(MDScrollView):
    manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Dashboard(MDScreen):
    pass


class Main(MDApp):

    # Variable global que contendrá self.root
    sm = None

    api_data = None
    
    data = None
    
    # indicamos donde se encuentra el archivo actual
    rutaPath = None
    
    rowDetails = None
    
    api = None
    
    url = None
    

    def build(self):
        # CreateDB()
        # Update()
        if platform in ['win', 'linux', 'macosx']:
            # resolución más común móvil
            Window.size = (414, 750)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.material_style = "M3"
        self.icon = "assets/pymeshield_favicon.png"
        self.title = "Pymeshield"
        self.sm = self.root
        self.rutaPath = Path(__file__).absolute().parent
        self.api = "http://192.168.224.241/api/"
        
    def update(self):
        Update()
        
    def get_api(self, url):
        url = self.api + url
        response = requests.get(url)
        data = json.loads(response.text)
        self.api_data = data['data']
        # self.insert_data();
        return self.api_data
    
    def get_api_data(self, url):
    
        url = self.api + url
        response = requests.get(url)
        data = json.loads(response.text)
        self.api_data = data
        # self.insert_data();
        return self.api_data

    def setRowDetails(self, row):
        self.rowDetails = row
        return self.rowDetails

    def rowPressed(self):
        return self.rowDetails

    def switch_screen(self, screen_name='login'):
        try:
            print('[*ALEIX*]: App.switch_screen called, screen: {}'.format(screen_name))
            self.sm.current = screen_name
            print('[*ALEIX*]: Setted the new screen')
        except:
            print('ERROR')
        else:
            print('success')
        finally:
            print('APPEAR')

    
if __name__ == '__main__':
    app = Main()
    app.run()
