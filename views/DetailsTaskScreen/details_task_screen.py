from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from utils import load_kv  # cargar ruta del script
from views.TaskScreen.task_screen import get_data_sqlite

load_kv(__name__)

class DetailsTaskScreen(MDScreen):
    
    def inici(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.switch_screen('dashboard')  # mostrar pantalla detalles tareas.
   
    def open(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.switch_screen('details_tasks')  # mostrar pantalla detalles tareas.

    id_tasca = ""  # creamos una variable vacia

    def on_enter(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        id_tasca = app.rowPressed()
        dataTareas = get_data_sqlite()
        # asignamos un valor a id_tasca accediendo con el parametro row y con id que es un campo del json
        id_tasca = int(id_tasca[6:])

        for i in dataTareas:  # recorremos los valores de la variable data2 que guarda los datos del json
            id = i['id']  # asignamos el nuevo valos a la variable id
            # asignamos un nuevo valor a la variable text recuperando datos del archivo json
            text = f"Tarea: {i['recommendation']}"
            text2 = f"Nivel de peligro: {i['danger']}"
            text3 = f"Gestión: {i['manages']}"

            self.ids.text1.text = text  # damos valor a la variable
            self.ids.text2.text = text2
            self.ids.text3.text = text3

            if id == id_tasca:  # comprovamos si id es igual a id_tasca
                break  # si los valores son iguales generamos un break en la ejecución del código