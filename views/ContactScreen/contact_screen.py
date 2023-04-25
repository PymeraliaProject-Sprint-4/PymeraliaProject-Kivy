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


class ContactScreen(MDScreen):

    def index(self):
        app = MDApp.get_running_app()
        app.switch_screen('dashboard')

    def on_enter(self):
        self.ids.text1.text = f"Pymeralia (Consultoría tecnológica | Pymeralia)"
        self.ids.text2.text = f"Email: hola@pymeralia.com"
        self.ids.text3.text = f"Telèfon: 977 74 40 87"
        self.ids.text4.text = f"Direcció: Av. dels Esports, 18, 43540 La Ràpita, Tarragona"
        self.ids.text5.text = f"Pàgina web: pymeralia.com"