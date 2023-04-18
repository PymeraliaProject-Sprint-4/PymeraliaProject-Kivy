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
from views.TaskScreen.task_screen import get_data_sqlite
import sqlite3

load_kv(__name__)


class DetailsTaskScreen(MDScreen):
    
    def inici(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.switch_screen('dashboard')  # mostrar pantalla detalles tareas.
   
    def open(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.switch_screen('details_tasks')  # mostrar pantalla detalles tareas.

    id_tasca = ""  # creamos una variable vacia

    def on_enter(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        id_tasca = app.rowPressed()
        dataTareas = get_data_sqlite()
        # asignamos un valor a id_tasca accediendo con el parametro row y con id que es un campo del json
        id_tasca = int(id_tasca[6:])

        for i in dataTareas:  # recorremos los valores de la variable data2 que guarda los datos del json
            id = i['id']  # asignamos el nuevo valos a la variable id
            # asignamos un nuevo valor a la variable text recuperando datos del archivo json
            text = f"{i['name']}"

            self.ids.desc.text = text  # damos valor a la variable

            if id == id_tasca:  # comprovamos si id es igual a id_tasca
                break  # si los valores son iguales generamos un break en la ejecución del código