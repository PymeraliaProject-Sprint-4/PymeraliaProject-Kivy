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
import sqlite3

load_kv(__name__)

# Esta clase es la clase que se encarga de las acciones que va a realizar el buscador.
class SearchE4(MDTextField): 
    pass

class TaskScreen(MDScreen):
    def calc(self, item):
        #variable que guarda el resultado el método getTareasData()
        data = self.get_data_sqlite()
            
        # Filtramos los datos según el texto de búsqueda
        search_results = [search_text for search_text in data if item.lower() in search_text['name'].lower()]

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
                    text = f"{result['name']}",
                    on_press = self.detalles
                    # secondary_text=f"Descripcion {result['descripcion']}",
                )
            )
            
    def get_data_sqlite(self):
        conn = sqlite3.connect('pymeshield.db')

        cursor = conn.cursor()
    
        cursor.execute('SELECT * FROM tasks')
        
        rows = cursor.fetchall()
        
        data = []
        
        for row in rows:
            data.append({
            'id': row[0],
            'name': row[1],
            'recommendation': row[2],
            'danger': row[3],
            'manages': row[4],
            'price': row[5],
            'price_customer': row[6]
            })

        self.data = data
        
        return self.data        
                
    def open(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.switch_screen('tasks') #mostrar pantalla tareas.
        
    def on_enter(self):
        data = self.get_data_sqlite()
        self.ids.tareas.clear_widgets()

        for i in data: #bucle que recorre el rango que le pasemos como parametro
            self.ids.tareas.add_widget( #añade widgets, despues de ids. va el id con el que podremos trabajar en el documento .kv
                ThreeLineIconListItem( #método que nos deja trabajar con 3 lineas que previamente lo hemos importado en la parte superior
                    IconLeftWidget( #método que nos permite agregar un icono
                        icon="clipboard-list"
                    ),
                    id = f"Tarea {i['id']}",
                    text = f"{i['name']}",
                    # secondary_text=f"Descripcion {i['descripcion']}", #línea 2
                    on_press = self.detalles
                )
            )# Lista que muestra las tareas
            
    def detalles(self,row): #inicializamos una función con el parametro row
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.setRowDetails(row.id)
        app.switch_screen('details_tasks') #mostrar detalles de la tarea.
        