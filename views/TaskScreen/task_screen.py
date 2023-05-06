from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import TwoLineIconListItem, IconLeftWidget
from utils import load_kv  # cargar ruta del script
import sqlite3

load_kv(__name__)

data = []


def get_data_sqlite():
    conn = sqlite3.connect("pymeshield.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    data = []

    for row in rows:
        data.append(
            {
                "id": row[0],
                "name": row[1],
                "recommendation": row[2],
                "danger": row[3],
                "manages": row[4],
                "price": row[5],
                "price_customer": row[6],
            }
        )

    data = data

    return data


class TaskScreen(MDScreen):
    tasks = []

    def calc(self, item):
        # variable que guarda el resultado el método getTareasData()
        if not self.tasks:
            return
        if hasattr(self, "search_event"):
            self.search_event.cancel()

        # Añadir delay
        self.search_event = Clock.schedule_once(
            lambda dt: self.hacer_busqueda(item), 0.5
        )

    def hacer_busqueda(self, item):
        # Borramos todos los elementos de la lista
        self.ids.tareas.clear_widgets()

        # Filtramos los datos según el texto de búsqueda
        search_results = filter(
            lambda x: (item.lower() in x["recommendation"].lower())
            or (item.lower() in x["danger"].lower()),
            self.tasks,
        )

        for result in search_results:
            self.ids.tareas.add_widget(
                TwoLineIconListItem(  # método que nos deja trabajar con 1 linea que previamente lo hemos importado en la parte superior
                    IconLeftWidget(  # método que nos permite agregar un icono
                        icon="clipboard-list"
                    ),
                    id=f"Tarea {result['id']}",
                    text=f"Tarea: {result['recommendation']}",
                    secondary_text=f"Nivel de peligro: {result['danger']}",
                    on_press=self.detalles,
                )
            )

    def open(self):
        self.manager.current = "tasks"  # mostrar pantalla tareas.

    def on_leave(self, *args):
        self.ids.tareas.clear_widgets()

    def on_enter(self):
        data = get_data_sqlite()

        for i in data:  # bucle que recorre el rango que le pasemos como parametro
            self.tasks.append(i)
            self.ids.tareas.add_widget(  # añade widgets, despues de ids. va el id con el que podremos trabajar en el documento .kv
                TwoLineIconListItem(  # método que nos deja trabajar con 3 lineas que previamente lo hemos importado en la parte superior
                    IconLeftWidget(  # método que nos permite agregar un icono
                        icon="clipboard-list"
                    ),
                    id=f"Tarea {i['id']}",
                    text=f"Tarea: {i['recommendation']}",
                    # línea 2
                    secondary_text=f"Nivel de peligro: {i['danger']}",
                    on_press=self.detalles,
                )
            )  # Lista que muestra las tareas

    def detalles(self, row):  # inicializamos una función con el parametro row
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.setRowDetails(row.id)
        self.manager.current = "details_tasks"  # mostrar detalles de la tarea.
