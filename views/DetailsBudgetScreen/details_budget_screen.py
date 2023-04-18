from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import OneLineIconListItem
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.utils import platform
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.uix.scrollview import MDScrollView
from kivy.clock import Clock
# import para crear listas (cambia dependiendo de los campos que queremos que tenga la lista), le pasamos diferentes imports de la misma biblioteca
from kivymd.uix.list import ThreeLineIconListItem, IconLeftWidget
import json  # importamos la libreria de python que nos permite trabajar con json
from pathlib import Path
from utils import load_kv  # cargar ruta del script
import sqlite3

load_kv(__name__)


class DetailsBudgetScreen(MDScreen):

    def inici(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.switch_screen('dashboard')  # mostrar pantalla detalles tareas.

    def get_data_sqlite(self):
        conn = sqlite3.connect('pymeshield.db')

        cursor = conn.cursor()
    
        cursor.execute('SELECT * FROM budgets')
        
        rows = cursor.fetchall()
        
        data = []
        
        for row in rows:
            data.append({
            'id': row[0],
            'price': row[1],
            'accepted': row[2],
            })

        self.data = data
        
        return self.data   

    def open(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        # mostrar pantalla detalles presupuestos.
        app.switch_screen('details_budgets')

    id_presu = ""  # creamos una variable vacia

    def on_enter(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        id_presu = app.rowPressed()
        dataPresu = self.get_data_sqlite()
        id_presu = int(id_presu[12:])

        for i in dataPresu:
            id = i['id']
            text = f"{i['price']}€ - {i['accepted']}"

            self.ids.desc.text = text

            if id == id_presu:
                break