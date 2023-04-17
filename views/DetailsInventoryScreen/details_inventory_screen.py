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
from utils import Notify
import requests
# import para crear listas (cambia dependiendo de los campos que queremos que tenga la lista), le pasamos diferentes imports de la misma biblioteca
from kivymd.uix.list import ThreeLineIconListItem, IconLeftWidget
import json  # importamos la libreria de python que nos permite trabajar con json
from pathlib import Path
from utils import load_kv  # cargar ruta del script

load_kv(__name__)


class DetailsInventoryScreen(MDScreen):

    def index(self):
        app = MDApp.get_running_app()
        app.switch_screen('dashboard') #mostrar detalles de la tarea.

    def on_enter(self):
        try:

            # Clear the text of the TextInput widgets
            self.ids.text1.text = ''
            self.ids.text2.text = ''
            self.ids.text3.text = ''
            self.ids.text4.text = ''
            self.ids.text5.text = ''
            self.ids.text6.text = ''
            self.ids.text7.text = ''

            # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
            app = MDApp.get_running_app()
            id_inventory = app.rowPressed()
            url = "http://localhost/api/devicelist"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            id_inventory = int(id_inventory)       
            

            for i in data:
                if i['id'] == id_inventory:
                    status = i['brand']
                    self.ids.text1.text = f"{i['brand']}"
                    self.ids.text2.text = f"{i['model']}"
                    self.ids.text3.text = f"{i['description']}"
                    self.ids.text4.text = f"{i['state']}"
                    self.ids.text5.text = f"{i['serial_number']}"
                    self.ids.text6.text = f"{i['mac_ethernet']}"
                    self.ids.text7.text = f"{i['mac_wifi']}"
                    break

        except Exception as e:
            # Handle any exceptions that may have occurred during the request.
            print(f"An error occurred: {e}")
            Notify(text="Error al recuperar los datos", snack_type='error').open()
