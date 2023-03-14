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

class QuestionaryScreen(MDApp):
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

            return Builder.load_file("questionary_screen.kv")  # importacion de estilos

    def on_start(self):  # creamos la clase on_start
        # Cargamos los datos desde el archivo data.json
        script_location = Path(__file__).absolute().parent
        with open(script_location / "informe_classes.json", "rt") as json_file:
            data = json.load(json_file)

        for i in data:  # bucle que recorre el rango que le pasemos como parametro
            self.root.ids.informes.add_widget(  # añade widgets, despues de ids. va el id con el que podremos trabajar en el documento .kv

                OneLineIconListItem(  # método que nos deja trabajar con 1 lineas que previamente lo hemos importado en la parte superior
                    IconLeftWidget(  # método que nos permite agregar un icono
                        icon="clipboard-file-outline"
                    ),
                    id = f"informe-{i['id']}",
                    text=f"{i['name']}",
                    on_press=self.print
                )
            )  # Lista que muestra los informes

    def buscar_informe(self, query):
        self.root.ids.informes.clear_widgets() # Limpiar la lista de informes antes de mostrar los resultados de búsqueda

        script_location = Path(__file__).absolute().parent
        with open(script_location / "informe_classes.json", "rt") as json_file:
            data = json.load(json_file)

        for i in data:
            if query.lower() in i['name'].lower(): # Verificar si el nombre del informe contiene la query
                self.root.ids.informes.add_widget(
                    OneLineIconListItem(
                        IconLeftWidget(
                            icon="clipboard-file-outline"
                        ),
                        id = f"informe-{i['id']}",
                        text=f"{i['name']}",
                        on_press=self.print
                    )
                )





myapp = QuestionaryScreen()
myapp.run()
