import json
from kivy.uix.image import Image, AsyncImage
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.card import MDCard
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
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from pathlib import Path #cargar ruta del script
from kivymd.uix.textfield import MDTextField
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

class DetailsQuestionaryScreen (MDApp):
    def build(self):
        self.title = "PymeShield"
        Window.size = (400, 600)
        scroll = ScrollView()
        self.sm = self.root

        list_view = MDList()
        for i in range(20):

            items = OneLineIconListItem(text=str(i) + ' item')
            list_view.add_widget(items)

        scroll.add_widget(list_view)

        return Builder.load_file("details_questionary_screen.kv")  # importacion de estilos

    id_informe = "";
    def print(self, row):
        id_informe = row.id
        print(f"Pressed {row.id}")
        self.root.ids["screen_manager"].current = 'Estat'
        script_location = Path(__file__).absolute().parent #indicamos donde se encuentra el archivo actual
        with open(script_location / "informe_classes.json", "rt") as json_file:
            data = json.load(json_file)

        print(f"Pressed {row.id[8:]}")

        img1 = 'Images/load.gif'
        img2 = 'Images/inprogress.gif'
        img3 = 'Images/done.gif'

        id_informe = int(row.id[8:])

        estat = "";
        for i in data:
            id = i['id']
            text=f"{i['name']} - {i['estat']}"

            self.root.ids.estatext.text = text

            if id == id_informe:
                estat = i['estat']
                break

        print(estat)

        if (estat == 'To do'):
            self.root.ids.imagen.source = img1

        if (estat == 'In progress'):
            self.root.ids.imagen.source = img2

        if (estat == 'Done'):
            self.root.ids.imagen.source = img3

myapp = DetailsQuestionaryScreen()
myapp.run()
