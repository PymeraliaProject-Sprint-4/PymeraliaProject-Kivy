from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from utils import load_kv  # cargar ruta del script
from views.BudgetScreen.budget_screen import get_data_sqlite

load_kv(__name__)

class DetailsBudgetScreen(MDScreen):

    def inici(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.switch_screen('dashboard')  # mostrar pantalla detalles tareas.

    def open(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        # mostrar pantalla detalles presupuestos.
        app.switch_screen('details_budgets')

    id_presu = ""  # creamos una variable vacia

    def on_enter(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        id_presu = app.rowPressed()
        dataPresu = get_data_sqlite()
        id_presu = int(id_presu[12:])

        for i in dataPresu:
            id = i['id']
            text = f"{i['price']}€ - {i['accepted']}"

            self.ids.desc.text = text

            if id == id_presu:
                break