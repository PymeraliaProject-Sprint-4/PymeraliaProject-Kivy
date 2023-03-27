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
import sqlite3


class SplashScreen(MDScreen):
    def on_enter(self, *args):
        Clock.schedule_once(self.switch_to_home, 5)

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

    api_data = None
    
    data = None
    
    # Variable global que contendrá les dades del JSON de dispositius
    dataJsonDevice = None
    
    # indicamos donde se encuentra el archivo actual
    rutaPath = None
    
    rowDetails = None
    
    api = None
    
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

    # def insert_data(self):
    #     conn = sqlite3.connect('pymeshield.db')

    #     cursor = conn.cursor()
        
    #     cursor.execute('DELETE FROM tasks')
        
    #     for i in self.api_data:
    #         id = int(i['id'])
    #         name = i['name']
    #         recommendation = i['recommendation']
    #         danger = i['peligro']
    #         manages = i['manages']
    #         price = i['price']
    #         price_customer = i['price_customer']
            
    #         datos = [(id, name, recommendation, danger, manages, price, price_customer)]
            
    #         for dato in datos:
    #             cursor.execute('INSERT INTO tasks (id, name, recommendation, danger, manages, price, price_customer) VALUES (?, ?, ?, ?, ?, ?, ?)', dato)


    #         conn.commit()
            
    #     conn.close()

    # def get_api(self, url):

    #     url = self.api + url
    #     response = requests.get(url)
    #     data = json.loads(response.text)
    #     self.api_data = data['data']
    #     self.insert_data();
    #     return self.api_data
            
    
    def get_api_data(self):
        conn = sqlite3.connect('pymeshield.db')

        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM tasks')
        
        rows = cursor.fetchall()
        
        data = []
        
        for row in rows:
            data.append({
            'id': row[0],
            'name': row[1],
            'recommendation': row[2],
            'danger': row[3],
            'manages': row[4],
            'price': row[5],
            'price_customer': row[6]
            })

        self.data = data
        
        return self.data

    def get_api_presu_data(self):
        url = "https://free-nba.p.rapidapi.com/players"
        querystring = {"page": "0", "per_page": "25"}
        headers = {
            "X-RapidAPI-Key": "2772911bd1msh8582a881fe2b605p18155cjsnd7cf86cd829d",
            "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
        }
        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        self.dataJsonPresu = data['data']
        return self.dataJsonPresu

    def get_api_devices(self):
        url = self.url + "devicelist"
        print(url)
        response = requests.get(url)
        data = json.loads(response.text)
        self.dataJsonDevice = []
        for i in range(len(data)):
            self.dataJsonDevice.append(data[i])
        return self.dataJsonDevice
      
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

    def getDeviceData(self):
        return self.get_api_devices()

if __name__ == '__main__':
    app = PymeApp()
    app.run()
