from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from utils import load_kv #cargar ruta del script
import requests

load_kv(__name__)

class DetailsQuestionaryScreen(MDScreen):

    def index(self):
        app = MDApp.get_running_app()
        app.switch_screen('dashboard') #mostrar detalles de la tarea.

    def on_enter(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        id_informe = app.rowPressed()
        url = "http://localhost/api/kivy/report"
        response = requests.get(url)
        data = response.json()

        print(f"Pressed {id_informe[8:]}")

        img2 = 'views/DetailsQuestionaryScreen/inprogress.gif'
        img3 = 'views/DetailsQuestionaryScreen/done.gif'

        id_informe = int(id_informe[8:])

        estat = "";
        for i in data:
            id = i['id']
            text=f"{i['name']} - {i['status']}"

            self.ids.estatext.text = text

            if id == id_informe:
                estat = i['status']
                break

        print(estat)

        if (estat == 'InProgress'):
            self.ids.imagen.source = img2

        if (estat == 'done'):
            self.ids.imagen.source = img3