from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from utils import load_kv  # cargar ruta del script
from views.BudgetScreen.budget_screen import get_data_sqlite

load_kv(__name__)


class DetailsBudgetScreen(MDScreen):
    def inici(self):
        self.manager.current = "budgets"

    def open(self):
        # mostrar pantalla detalles presupuestos.
        self.manager.current = "details_budgets"

    id_presu = ""  # creamos una variable vacia

    def on_enter(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        id_presu = app.rowPressed()
        dataPresu = get_data_sqlite()
        id_presu = int(id_presu[12:])

        for i in dataPresu:
            id = i["id"]
            text = f"Presupuesto número {i['id']}"
            text2 = f"Total presupuesto: {i['price']} €"
            text3 = f"Aceptado: {i['accepted']}"

            self.ids.text1.text = text
            self.ids.text2.text = text2
            self.ids.text3.text = text3

            if id == id_presu:
                break
