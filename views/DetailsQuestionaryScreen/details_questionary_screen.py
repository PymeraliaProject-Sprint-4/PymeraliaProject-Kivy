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
import os

load_kv(__name__)

class DetailsQuestionaryScreen(MDScreen):

    def index(self):
        app = MDApp.get_running_app()
        app.switch_screen('dashboard') #mostrar detalles de la tarea.

    def on_enter(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        id_informe = app.rowPressed()
        script_location = Path(__file__).absolute().parent #indicamos donde se encuentra el archivo actual
        with open(script_location / "informe_classes.json", "rt") as json_file:
            data = json.load(json_file)

        print(f"Pressed {id_informe[8:]}")

        img1 = 'views/DetailsQuestionaryScreen/load.gif'
        img2 = 'views/DetailsQuestionaryScreen/inprogress.gif'
        img3 = 'views/DetailsQuestionaryScreen/done.gif'

        id_informe = int(id_informe[8:])

        estat = "";
        for i in data:
            id = i['id']
            text=f"{i['name']} - {i['estat']}"

            self.ids.estatext.text = text

            if id == id_informe:
                estat = i['estat']
                break

        print(estat)

        if (estat == 'To do'):
            self.ids.imagen.source = img1

        if (estat == 'In progress'):
            self.ids.imagen.source = img2

        if (estat == 'Done'):
            self.ids.imagen.source = img3