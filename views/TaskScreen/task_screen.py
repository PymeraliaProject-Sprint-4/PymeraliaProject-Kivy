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

# Esta clase es la clase que se encarga de las acciones que va a realizar el buscador.
class SearchE4(MDTextField): 
    pass

class TaskScreen(MDScreen):
    def calc(self, item):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        #variable que guarda el resultado el método getTareasData()
        dataTareas = app.getTareasData()
            
        # Filtramos los datos según el texto de búsqueda
        search_results = [search_text for search_text in dataTareas if item.lower() in search_text['name'].lower()]

        # Actualizamos la lista de resultados de búsqueda en la interfaz de usuario
        search_results_list = self.ids.tareas
        # Borramos todos los elementos de la lista
        search_results_list.clear_widgets()

        for result in search_results:
            search_results_list.add_widget(
                OneLineIconListItem( #método que nos deja trabajar con 1 linea que previamente lo hemos importado en la parte superior
                    IconLeftWidget( #método que nos permite agregar un icono
                        icon="clipboard-list"
                    ),
                    
                    id = f"Tarea {result['id']}",
                    text = f"Tarea {result['name']}",
                    secondary_text=f"Descripcion {result['descripcion']}",
                )
            )
            
    def open(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.switch_screen('tasks') #mostrar pantalla tareas.
    
    def on_enter(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        dataTareas = app.getTareasData()

        for i in dataTareas: #bucle que recorre el rango que le pasemos como parametro
            self.ids.tareas.add_widget( #añade widgets, despues de ids. va el id con el que podremos trabajar en el documento .kv
                ThreeLineIconListItem( #método que nos deja trabajar con 3 lineas que previamente lo hemos importado en la parte superior
                    IconLeftWidget( #método que nos permite agregar un icono
                        icon="clipboard-list"
                    ),
                    
                    id = f"Tarea {i['id']}",
                    text = f"Tarea {i['name']}",
                    secondary_text=f"Descripcion {i['descripcion']}", #línea 2
                    on_press = self.detalles
                )
            )# Lista que muestra las tareas
            
    def detalles(self,row): #inicializamos una función con el parametro row
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.rowDetails(row.id)
        app.switch_screen('details_tasks') #mostrar detalles de la tarea.
        