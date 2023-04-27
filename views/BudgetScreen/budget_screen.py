from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import OneLineIconListItem, ThreeLineIconListItem, IconLeftWidget
from kivymd.uix.screen import MDScreen
from utils import load_kv  # cargar ruta del script
import sqlite3

load_kv(__name__)

# Esta clase es la clase que se encarga de las acciones que va a realizar el buscador.

data = []

def get_data_sqlite():
    conn = sqlite3.connect('pymeshield.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM budgets')
    
    rows = cursor.fetchall()
    
    data = []
    
    for row in rows:
        data.append({
        'id': row[0],
        'price': row[1],
        'accepted': row[2],
        })

    data = data
    
    return data    

class SearchE4(MDTextField):
    pass


class BudgetScreen(MDScreen):
    def calc(self, item):
        # variable que guarda el resultado el método getTareasData()
        data = get_data_sqlite()

        # Filtramos los datos según el precio de búsqueda
        search_results = [search_text for search_text in data if str(item) in str(search_text['price'])]

        # Actualizamos la lista de resultados de búsqueda en la interfaz de usuario
        search_results_list = self.ids.presupuesto
        # Borramos todos los elementos de la lista
        search_results_list.clear_widgets()

        for result in search_results:
            search_results_list.add_widget(
                OneLineIconListItem(  # método que nos deja trabajar con 1 linea que previamente lo hemos importado en la parte superior
                    IconLeftWidget(  # método que nos permite agregar un icono
                        icon="account-cash"
                    ),
                    
                    id=f"Presupuesto {result['id']}",
                    text=f"{result['price']}€",
                    secondary_text=f"{result['accepted']}",  # línea 2
                    on_press=self.detalles
                )
            )      
        
    def open(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.switch_screen('budgets')  # mostrar pantalla tareas.

    def on_enter(self):
        data = get_data_sqlite()

        self.ids.presupuesto.clear_widgets()

        for i in data:  # bucle que recorre el rango que le pasemos como parametro
            self.ids.presupuesto.add_widget(  # añade widgets, despues de ids. va el id con el que podremos trabajar en el documento .kv
                ThreeLineIconListItem(  # método que nos deja trabajar con 3 lineas que previamente lo hemos importado en la parte superior
                    IconLeftWidget(  # método que nos permite agregar un icono
                        icon="account-cash"
                    ),

                    id=f"Presupuesto {i['id']}",
                    text=f"{i['price']}€",
                    secondary_text=f"{i['accepted']}",  # línea 2
                    on_press=self.detalles
                )
            )  # Lista que muestra las tareas

    def detalles(self, row):  # inicializamos una función con el parametro row
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.setRowDetails(row.id)
        app.switch_screen('details_budgets')  # mostrar detalles de la tarea.