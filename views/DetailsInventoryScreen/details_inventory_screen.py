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
from views.InventoryScreen.inventory_screen import get_data_sqlite
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
    
    def goBack(self, screen):
        self.manager.current = screen

    def on_enter(self):
        try:

            # Elimina el texto de los ids en la pantalla de detalles antes de mostrar el texto de otro dispositivo
            widget_ids = ['text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7']
            for widget_id in widget_ids:
                self.ids[widget_id].text = ''

            # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
            app = MDApp.get_running_app()
            id_inventory = app.rowPressed()
            data = get_data_sqlite()
            id_inventory = int(id_inventory)       
            

            for i in data:
                if i['id'] == id_inventory:
                    status = i['brand']
                    self.ids.text1.text = f"Marca: {i['brand']}"
                    self.ids.text2.text = f"Modelo: {i['model']}"
                    self.ids.text3.text = f"Descripción del dispositivo: {i['description']}"
                    self.ids.text4.text = f"Estado del dispositivo: {i['state']}"
                    self.ids.text5.text = f"Número de serie: {i['serial_number']}"
                    self.ids.text6.text = f"MAC Ethernet: {i['mac_ethernet']}"
                    self.ids.text7.text = f"MAC Wifi: {i['mac_wifi']}"
                    break
                else:
                    self.ids.text1.text = "Este dispositivo aún no está registrado o NO le pertenece, porfavor pruebe de escanear un código QR válido."
                

        except Exception as e:
            # Handle any exceptions that may have occurred during the request.
            print(f"An error occurred: {e}")
            Notify(text="Error al recuperar los datos", snack_type='error').open()
    
    def open_camera(self, *args):
        app = MDApp.get_running_app()
        self.manager.current = "QR"