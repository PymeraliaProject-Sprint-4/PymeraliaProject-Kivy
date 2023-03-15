from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.utils import platform
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.uix.scrollview import MDScrollView
from kivy.clock import Clock
import json  # importamos la libreria de python que nos permite trabajar con json
from pathlib import Path  # cargar ruta del script
import requests


class SplashScreen(MDScreen):
    def on_enter(self, *args):
        Clock.schedule_once(self.switch_to_home, 2)

    def switch_to_home(self, dt):
        app = MDApp.get_running_app()
        app.switch_screen('login')


class ContentNavigationDrawer(MDScrollView):
    manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Dashboard(MDScreen):
    pass


class PymeApp(MDApp):

    # Variable global que contendrá self.root
    sm = None
    # Variable global que contendrá les dades del JSON de presupostos
    dataJsonPresu = None
    # Variable global que contendrá les dades del JSON de tasques
    dataJsonTask = None
    # indicamos donde se encuentra el archivo actual
    rutaPath = None

    rowDetails = None
    
    url = None

    def build(self):
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
        self.url = "http://localhost/api/"

    def get_api_task_data(self):
        url = self.url + "all-data"
        print(url)
        response = requests.get(url)
        data = json.loads(response.text)
        self.dataJsonTask = data['data']
        return self.dataJsonTask
    
    def get_api_presu_data(self):
        url = "https://free-nba.p.rapidapi.com/players"
        querystring = {"page":"0","per_page":"25"}
        headers = {
            "X-RapidAPI-Key": "2772911bd1msh8582a881fe2b605p18155cjsnd7cf86cd829d",
            "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        self.dataJsonPresu = data['data']
        return self.dataJsonPresu

    def setRowDetails(self, row):
        self.rowDetails = row
        return self.rowDetails

    def rowPressed(self):
        print(self.rowDetails)
        return self.rowDetails

    def switch_screen(self, screen_name='login'):
        self.sm.current = screen_name

    # Método que utilizaremos para recoger los datos del Json de Tareas y guardarlos
    def getTareasData(self):
        return self.get_api_task_data()

    # Método que utilizaremos para recoger los datos del Json de Presupuestos y guardarlos
    def getPresuData(self):
        return self.get_api_presu_data()


if __name__ == '__main__':
    app = PymeApp()
    app.run()
