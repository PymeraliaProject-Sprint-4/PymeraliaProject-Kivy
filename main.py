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

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        script_location = Path(__file__).absolute().parent #indicamos donde se encuentra el archivo actual
        with open(script_location / "informe_classes.json", "rt") as f:
            self.data = json.load(f)
        self.search_field = MDTextField(hint_text="Search")
        self.search_field.bind(text=self.search)
        self.add_widget(self.search_field)

    def search(self, instance, value):
        result = [item for item in self.data if value in item["name"]]
        # show the result in a way you prefer, e.g.
        for item in result:
            print("Name:", item["name"])


class ContentNavigationDrawer(MDBoxLayout):
    manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class MyApp (MDApp):
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

        return Builder.load_file("main2.kv")  # importacion de estilos

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





myapp = MyApp()
myapp.run()
