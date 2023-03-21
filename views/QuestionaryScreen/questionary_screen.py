from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import IconLeftWidget
from utils import load_kv
import requests

load_kv(__name__)


class QuestionaryScreen(MDScreen):
    def open(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.switch_screen('questionary')  # mostrar pantalla tareas.

    def on_enter(self):
        self.ids.informes.clear_widgets()
        # Cargamos los datos desde la respuesta de la API
        self.getReports()

    def getReports(self):
        url = "http://localhost/api/kivy/report"
        response = requests.get(url)
        data = response.json()

        reports = []

        for reports in data:  # bucle que recorre el rango que le pasemos como parametro
            self.ids.informes.add_widget(  # añade widgets, despues de ids. va el id con el que podremos trabajar en el documento .kv

                OneLineIconListItem(  # método que nos deja trabajar con 1 lineas que previamente lo hemos importado en la parte superior
                    IconLeftWidget(  # método que nos permite agregar un icono
                        icon="clipboard-file-outline"
                    ),
                    id=f"informe-{reports['id']}",
                    text=f"{reports['name']}",
                    on_press=self.print
                )
            )  # Lista que muestra los informes

        return reports

    def buscar_informe(self, query):
        # Limpiar la lista de informes antes de mostrar los resultados de búsqueda
        self.ids.informes.clear_widgets()

        url = "http://localhost/api/kivy/report"
        response = requests.get(url)
        data = response.json()

        for i in data:
            # Verificar si el nombre del informe contiene la query
            if query.lower() in i['name'].lower():
                self.ids.informes.add_widget(
                    OneLineIconListItem(
                        IconLeftWidget(
                            icon="clipboard-file-outline"
                        ),
                        id=f"informe-{i['id']}",
                        text=f"{i['name']}",
                        on_press=self.print
                    )
                )

    def print(self, row):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.setRowDetails(row.id)
        # mostrar detalles de la tarea.
        app.switch_screen('details_questionary')
