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
from kivymd.uix.list import ThreeLineIconListItem, IconLeftWidget #import para crear listas (cambia dependiendo de los campos que queremos que tenga la lista), le pasamos diferentes imports de la misma biblioteca
import json #importamos la libreria de python que nos permite trabajar con json
from pathlib import Path
from utils import load_kv #cargar ruta del script

load_kv(__name__)

class DetailsBudgetScreen(MDScreen):

    def open(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.switch_screen('details_budgets') #mostrar pantalla detalles presupuestos.
        
    id_presu = "" #creamos una variable vacia
    def on_enter(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        id_presu = app.rowPressed()
        print(f"Pressed {id_presu}") #imprimimos el valor
        dataPresu = app.getPresuData()
        id_presu = id_presu[10:]
        print(id_presu)

        for i in dataPresu:
            id = i['id']
            text= f"{i['name']} - {i['preu']} - {i['data']}"

            self.ids.desc.text = text

            if id == id_presu:
                break
